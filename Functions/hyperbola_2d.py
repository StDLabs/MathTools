import numpy as np
from MathTools.PlotVisualize.plot_sets_of_functions_2d import plot_sets_of_functions_2d
from MathTools.Functions.line_2d import line_2d


def hyperbola_2d(W: list, input_type: int, a: float, b: float, n) -> [list, list]:
    """
    The hyperbola_2d function is designed to generate points on a 2D hyperbola curve based on the provided parameters

    :param W: A list containing the parameters that define the hyperbola curve. The interpretation of this list depends
        on the value of input_type.
    :param input_type: input_type = 0 means W = [A0, A1, A2, N] - parameters of hyperbola F = A1*(X + A2)**(-N) + A0.
        [a, b] must not include the infinity.
    :param a: left boundary
    :param b: right boundary
    :param n: number of points
    :return: F = [F0, F1, ...], X = [X0, X1, ...] - points of hyperbola
    """

    if input_type == 0:
        h = (b - a) / (n - 1)
        X = np.array([a + h * i for i in range(0, n)])
        F = W[1] * ((X + W[2]) ** (-W[3])) + W[0]

    return F, X


def hyperbola_2d_example():

    F1, X1 = hyperbola_2d(W=[2, 3.5, 1, 1], input_type=0, a=-0.75, b=1, n=100)
    F2, X2 = hyperbola_2d(W=[2, 3.5, 1, 1], input_type=0, a=-3, b=-1.25, n=100)
    F3, X3 = line_2d(W=['x', 2], input_type=2, a=-3, b=1, n=50)
    F4, X4 = line_2d(W=['y', -1], input_type=2, a=-15, b=15, n=50)

    S = {'F1': {'F': F1, 'X': X1, 'T': 'Dash', 'Label': 'W=[2, 3.5, 1, 1] right', 'Color': 'r', 'Line width': 1},
         'F2': {'F': F2, 'X': X2, 'T': 'Line', 'Label': 'W=[2, 3.5, 1, 1] left', 'Color': 'b', 'Line width': 1},
         'F3': {'F': F3, 'X': X3, 'T': 'Dash', 'Label': 'W=[x, 2] asymptote', 'Color': 'c', 'Line width': 2},
         'F4': {'F': F4, 'X': X4, 'T': 'Line', 'Label': 'W=[y, -1] asymptote', 'Color': 'y', 'Line width': 2.2}}
    W = {'W1': {'S': S, 'ttl': 'Title', 'axisX': 'axisX1', 'axisY': 'axisY1'}}
    plot_sets_of_functions_2d(W, False, True, False, 13)

    return
