import math as m
from MathTools.PlotVisualize.PlaneMapping.plot_sets_of_functions_2d import plot_sets_of_functions


def gauss(sigma: float, mx: float, a: float, b: float, n: int) -> [list, list]:
    """
    The gauss_1d function computes the values of the one-dimensional Gaussian (normal) probability
    distribution function over a specified range

    :param sigma: The standard deviation of the Gaussian distribution
    :param mx: The mean (expectation) of the Gaussian distribution
    :param a: left boundary
    :param b: right boundary
    :param n: number of points
    :return: F = [F0, F1, ...], X = [X0, X1, ...] - points of the gauss function
    """

    h = (b - a) / (n - 1)
    X = [a + h * i for i in range(0, n)]
    F = [(1 / (sigma * m.sqrt(2 * m.pi))) * m.exp(-0.5 * (((X[i] - mx) / sigma) ** 2)) for i in range(0, n)]

    return F, X


def gauss_example():

    F1, X1 = gauss(2, 3, -3, 9, 100)

    S = {'F1': {'F': F1, 'X': X1, 'T': 'Line', 'Label': 'Gauss', 'Color': 'r', 'Line width': 1}}
    W = {'W1': {'S': S, 'ttl': 'Title', 'axisX': 'axisX1', 'axisY': 'axisY1'}}
    plot_sets_of_functions(W, False, True, False, 13)

    return
