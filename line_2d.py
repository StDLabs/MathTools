from MathTools.math_dicts import dict_directions
import numpy as np


def line_2d(W: list, input_type: int, a: float, b: float, n: int) -> [list, list]:
    """

    :param W: list of all input parameters of the line
    :param input_type: input_type = 0 means W = [B, k] - parameters of a line f = k*x + B.
                       input_type = 1 means W = [M0, M1] - line trough two points M0 = [f0, x0], M1 = [f1, x1].
                       input_type = 2 means W = [s, p]. s - name of axis Ox or Oy (see dict_directions)
                       a, b, N refer to the axis. p - coordinate of intersection.
    :param a: left boundary
    :param b: right boundary
    :param n: number of points
    :return: F = [F0, F1, ...], X = [X0, X1, ...] - points of the line
    """

    if input_type == 0:
        k = W[1]
        B = W[0]
    if input_type == 1:
        DF = (W[1][1] - W[0][1])
        k = (W[1][0] - W[0][0]) / DF
        B = (W[1][1] * W[0][0] - W[0][1] * W[1][0]) / DF

    h = (b - a) / (n - 1)
    S = [a + h * i for i in range(0, n)]

    if (input_type == 0) | (input_type == 1):
        X = S
        F = [k * X[i] + B for i in range(0, n)]

    if input_type == 2:
        s = dict_directions(W[0])
        P = W[1] * np.ones(n)
        SP = [P, S]
        X = SP[int(not s)]
        F = SP[s]

    return F, X
