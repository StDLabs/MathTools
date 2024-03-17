from MathTools.math_dicts import dict_directions
import numpy as np


def line_2d(W: list, input_type: int, a: float, b: float, n: int) -> [list, list]:
    """
    The purpose of the function is to calculate the line equation based on the provided input parameters
    (W and input_type), and then generate a set of points along that line within the specified boundaries (a and b)
    with the desired number of points (n).

    :param W: A list containing the input parameters that define the line
    :param input_type: An integer value that specifies how the line is defined (0, 1, or 2)
        input_type = 0 means W = [B, k] - contains the slope (k) and y-intercept (B) of the line in the form f = k*x + B
        input_type = 1 means W = [M0 = [f0, x0], M1 = [f1, x1]] - contains two points through which the line passes.
        input_type = 2 means W = [s, p]. s - contains the name of the axis (s) and the coordinate
            of the intersection point (p) (see dict_directions),
            where a, b, n refer to the s-axis. p - coordinate of intersection.
    :param a: The left boundary of the line segment
    :param b: The right boundary of the line segment
    :param n: The number of points to generate along the line segment
    :return: F = [F0, F1, ...], X = [X0, X1, ...] - The function returns two lists: F and X,
        representing the y-coordinates and x-coordinates, respectively, of the points along the line segment
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
