# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['ihu', 'y_der', 'check_for_stupidity']

# Cell
from scipy.integrate import solve_ivp
from numpy.random import random_sample
from numpy import array, linspace
from math import sqrt
from .herm import rand_herm_ndarray, test_herm_ndarray
from .unitary import rand_unitary_ndarray, test_unitary_ndarray

# Cell
def ihu(ham_func, u0, T, no_time_step_for_eval, **kwargs):
    r"""evolves the unitary

    Parameters
    ----------
    ham_func : function
        Function which produces the Hamiltonian
        as it appears at time t
        form ham_func(t)
    u0 : ndarray
        Unitary at time 0
    T : float
        Evolution time
    no_time_step_for_eval : int
        no of time steps for evaluation in the
        final output
    **kwargs
        Arbitrary optional keyword arguments.
        w : float
            Defaults to 6.28

    Returns
    -------
    Bunch object with the following fields defined:
    t  : [ndarray, shape (n_points,)]
        Time points.
    y  : [ndarray, shape (n, n_points)]
        Values of the solution at t.
    sol: [OdeSolution or None]
        Found solution as OdeSolution instance; None if
        dense_output was set to False.
    t_events: [list of ndarray or None]
        Contains for each event type a list of arrays at which an event of
        that type event was detected. None if events was None.
    nfev: [int]
        Number of evaluations of the right-hand side.
    njev: [int]
        Number of evaluations of the Jacobian.
    nlu :[int]
        Number of LU decompositions.
    status [int]
        Reason for algorithm termination:
        • -1: Integration step failed.
        • 0: The solver successfully reached the end of tspan.
        • 1: A termination event occurred.
    message: [string]
        Human-readable description of the termination reason.
    success: [bool]
        True if the solver reached the interval end or a
        termination event occurred (status
    >= 0).

    u_series :[ndarray, shape (sqrt(n), sqrt(n), n_points)]
        Values of the solution at t.

    """
    u_shape = u0.shape()

    check_for_stupidity(ham_func, u0, )
    T = evolution_time
    Nt = no_time_step_for_eval
    dt = T/Nt
    y0 = u0.ravel()
    t_eval_span = linspace(0, T, Nt)

    result = solve_ivp(fun=y_der, t_span=(0, T), y0=y0,
                       t_eval=t_eval_span, args=(u_shape, ham_func))
    # Will expose other options later on

    print(result.message)

    u_series = result.y.reshape(u_shape, u_shape, result.y.shape[-1])

    return u_series, result


# Cell
def y_der(t, y, u_shape, ham_func):
    r"""Basically dy/dt

    Does some stuff.

    Parameters
    ----------
    t : float
        Current time value during the integration
    y : ndarray
        flattened unitary at the current time

    Returns
    -------
    dydt : ndarray
        flattened derivative of the unitary

    """
    # u_shape = int(sqrt(y.shape(0)))
    u_curr = y.reshape(u_shape, u_shape)
    hamiltonian_curr = ham_func(t)
    dudt = -1j*hamiltonian_curr@u_curr
    dydt = dudt.ravel()

    return dydt

# Cell
def check_for_stupidity(ham_func, u0, ):
    r"""Perform checks for invalid inputs and the lot"""
    u0_shape = u0.shape()
    ham_shape = ham_func(0.2).shape()


    try:
        assert u0_shape[0] == u0_shape[1]
    except AssertionError as e1:
        print('Initial unitary is not a square matrix')
        raise AssertionError

    try:
        assert ham_shape[0] == ham_shape[1]
    except AssertionError as e2:
        print('Hamiltonian is not a square matrix')
        raise AssertionError

    try:
        assert u0_shape == ham_shape
    except AssertionError as e3:
        print('Hamiltonian shape is not same as that of the initial unitary.')
        raise AssertionError

    try:
        assert test_unitary_ndarray(u0) is True
    except AssertionError as e4::
        print('Initial unitary is not unitary')
        raise AssertionError

    try:
        assert test_herm_ndarray(ham_func(0.42)) is True
    except AssertionError as e4::
        print('Hamiltonian is not Hermitian')
        raise AssertionError



    return None