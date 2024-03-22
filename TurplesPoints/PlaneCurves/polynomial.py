import numpy as np
from MathTools.PlotVisualize.PlaneMapping.plot_sets_of_functions_2d import plot_sets_of_functions


def polynomial(A: list, a: float, b: float, n: int) -> [list, list]:
    """
    The polynomial_2d function is designed to generate points on a 2D polynomial curve based on
    the provided coefficients and boundaries

    :param A: A list containing the coefficients of the polynomial, where A[0] is the constant term,
        A[1] is the coefficient of x, A[2] is the coefficient of x^2, and so on.
        A = [A0, A1, ...] - parameters of a polynomial F = A0 + A1*x + A2*x**2 + ...
    :param a: left boundary
    :param b: right boundary
    :param n: number of points
    :return: F = [F0, F1, ...], X = [X0, X1, ...] - points of polynomial
    """

    L = len(A)
    A = np.array(A)

    h = (b - a) / (n - 1)
    X = np.array([a + h * i for i in range(0, n)])

    # MX = [[1,         1,         1,         ..., 1             ],
    #       [X0,        X1,        X2,        ..., X_(N-1)       ],
    #       [X0**2,     X1**2,     X2**2,     ..., X_(N-1)**2    ],
    #       [                        ...                         ],
    #       [X0**(L-1), X1**(L-1), X2**(L-1), ..., X_(N-1)**(L-1)]]
    MX = [np.ones(n)]
    for i in range(1, L):
        MX.append(X ** i)
    MX = np.array(MX)

    MX = np.transpose(MX)
    AMX = A * MX
    F = [AMX[i].sum() for i in range(0, n)]
    X = list(X)

    return F, X


def polynomial_example():

    A = [2, -3, -5, 7, -2, 8]
    F1, X1 = polynomial(A, a=-1, b=1, n=100)

    S = {'F1': {'F': F1, 'X': X1, 'T': 'Line', 'Label': 'A = [2, -3, -5, 7, -2, 8]', 'Color': 'r', 'Line width': 1}}
    W = {'W1': {'S': S, 'ttl': 'Title', 'axisX': 'axisX1', 'axisY': 'axisY1'}}
    plot_sets_of_functions(W, False, True, False, 13)

    return
