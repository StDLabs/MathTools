import numpy as np


def odd_polynomial(A: list, a: float, b: float, n: int) -> [list, list]:
    """
    The odd_polynomial_2d function is designed to generate points on a 2D polynomial curve
    where the exponents of the variable are odd numbers. Supports polynomial curves of any odd degree
    by accepting a list of coefficients

    :param A: A = [A0, A1, ...] - parameters of a polynomial F = A0 + A1*x + A2*x**3 + ...
    :param a: left boundary
    :param b: right boundary
    :param n: number of points
    :return: F = [F0, F1, ...], X = [X0, X1, ...] - points of polynomial
    """

    L = len(A)
    A = np.array(A)

    h = (b - a) / (n - 1)
    X = np.array([a + h * i for i in range(0, n)])

    # MX = [[1,          1,          1,          ..., 1              ],
    #       [X0,         X1,         X2,         ..., X_(N-1)        ],
    #       [X0**3,      X1**3,      X2**3,      ..., X_(N-1)**3     ],
    #       [                           ...                          ],
    #       [X0**(2L-3), X1**(2L-3), X2**(2L-3), ..., X_(N-1)**(2L-3)]]
    MX = [np.ones(n)]
    for i in range(1, L):
        MX.append(X ** (2 * i - 1))
    MX = np.transpose(MX)

    AMX = A * MX
    F = [AMX[i].sum() for i in range(0, n)]
    X = list(X)

    return F, X
