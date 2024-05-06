import numpy as np
import math as m
from MathTools.PlotVisualize.PlaneMapping.plot_sets_of_functions_2d import plot_sets_of_functions
from MathTools.PointGenerators.PlaneCurves.line_2d import line_2d


def logarithm_nat(W: list, a: float, b: float, n: int) -> [list, list]:
    """
    The ln_2d function is designed to generate points on a 2D natural logarithmic curve based on the provided parameters

    :param W: list of all input parameters of natural logarithm.
        W = [A0, A1, A2] - coefficients for logarithmic function F = A1*Ln(X + A2) + A0.
        [a, b] must not include the infinity.
    :param a: left boundary
    :param b: right boundary
    :param n: number of points
    :return: F = [F0, F1, ...], X = [X0, X1, ...] - points of natural logarithm
    """

    h = (b - a) / (n - 1)
    X = np.array([a + h * i for i in range(0, n)])
    F = [W[1] * m.log(X[i] + W[2]) + W[0] for i in range(0, n)]

    return F, X


def logarithm_nat_example():

    F1, X1 = logarithm_nat(W=[1, 2, 1], a=-0.75, b=3, n=100)
    F2, X2 = line_2d(W=['y', -1], input_type=2, a=-2, b=4, n=50)

    S = {'F1': {'F': F1, 'X': X1, 'T': 'Dash', 'Label': 'W=[1, 2, 1]', 'Color': 'r', 'Line width': 1},
         'F2': {'F': F2, 'X': X2, 'T': 'Line', 'Label': 'W=[y, -1] asymptote', 'Color': 'b', 'Line width': 1}}
    W = {'W1': {'S': S, 'ttl': 'Title', 'axisX': 'axisX1', 'axisY': 'axisY1'}}
    plot_sets_of_functions(W, False, True, False, 13)

    return
