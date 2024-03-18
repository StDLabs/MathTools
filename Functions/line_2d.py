import numpy as np
from MathTools.math_dicts import dict_directions
from MathTools.PlotVisualize.plot_sets_of_functions_2d import plot_sets_of_functions_2d


def line_2d(W: list, input_type: int, a: float, b: float, n: int) -> [list, list]:
    """
    The purpose of the function is to calculate the line equation based on the provided input parameters
    (W and input_type), and then generate a set of points along that line within the specified boundaries (a and b)
    with the desired number of points (n). [Analytical geometry / Functions]

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
        X = list(SP[int(not s)])
        F = list(SP[s])

    return F, X


def line_2d_example():

    F1, X1 = line_2d(W=[3, -1], input_type=0, a=-5, b=5, n=50)
    F2, X2 = line_2d(W=[5, -2], input_type=0, a=-5, b=5, n=50)
    F3, X3 = line_2d(W=[[1, 2], [-3, -4]], input_type=1, a=-5, b=5, n=50)
    F4, X4 = line_2d(W=['x', -2], input_type=2, a=-5, b=5, n=50)
    F5, X5 = line_2d(W=['y', -3], input_type=2, a=-5, b=5, n=50)

    S = {'F1': {'F': F1, 'X': X1, 'T': 'Dash', 'Label': 'W=[3, -1]', 'Color': 'r', 'Line width': 1},
         'F2': {'F': F2, 'X': X2, 'T': 'Line', 'Label': 'W=[5, -2]', 'Color': 'b', 'Line width': 1.2},
         'F3': {'F': F3, 'X': X3, 'T': 'Line', 'Label': 'W=[[1, 2], [-3, -4]]', 'Color': 'k', 'Line width': 1.5},
         'F4': {'F': F4, 'X': X4, 'T': 'Dash', 'Label': 'W=[x, -2]', 'Color': 'c', 'Line width': 2},
         'F5': {'F': F5, 'X': X5, 'T': 'Line', 'Label': 'W=[y, -3]', 'Color': 'y', 'Line width': 2.2},
         'F6': {'F': [1, -3], 'X': [2, -4], 'T': 'Dots', 'Label': '[1, 2], [-3, -4]', 'Color': 'k', 'Line width': 1.5}}
    W = {'W1': {'S': S, 'ttl': 'Title', 'axisX': 'axisX1', 'axisY': 'axisY1'}}
    plot_sets_of_functions_2d(W, False, True, False, 13)

    return
