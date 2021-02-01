# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['ihu', 'y_der']

# Cell
from scipy.integrate import solve_ivp
from numpy.random import random_sample
from numpy import array

# Cell
def ihu(ham_func, u0, T, no_time_step_for_eval, **kwargs):
    r"""evolves the unitary

    Steps:
    - Determines Shape of U0.
    - Determines Shape of H (at any random time t).
    - If anyone of U, H are non square exit.
    - If shapes match proceed else exit.
    - make sure Output of H is Hermitian
      (by trying it out at 3 different times)
    - Initialize inputs T, Nt
    - Flatten u0 to get y0
    - calculate dt = T/ Nt
    - make y_der
    - evolve y
    - collect results
    - y_series to u_series
    - print messages
    - return stuff + useries



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
    w = kwargs.pop("w", 6.28)
    if kwargs:
        print("Got {0} unused kwargs".format(len(kwargs)))
    return (x**2 + len(y)) * (w + z)


# Cell
def y_der(x, yevolver, z=3.14, **kwargs):
    r"""Some function

    Does some stuff.

    Parameters
    ----------
    x : int
        Description of x
    y : str
        Description of y
    z : float, optional
        Description of z.  Defaults to 3.14
    **kwargs
        Arbitrary optional keyword arguments.
        w : float
            Defaults to 6.28

    Returns
    -------
    double
        Some nonsensical number computed from some ugly formula

    """
    w = kwargs.pop("w", 6.28)
    if kwargs:
        print("Got {0} unused kwargs".format(len(kwargs)))
    return (x**2 + len(y)) * (w + z)