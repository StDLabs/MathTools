from MathTools.math_dicts import dict_directions
import copy
from MathTools.RandomDistribValues.Variables.even_distrib import even_distrib
from MathTools.PointGenerators.PlaneCurves.polynomial import polynomial
from MathTools.PlotVisualize.PlaneMapping.plot_sets_of_functions_2d import plot_sets_of_functions


def add_simple_noise(W: list, axis, d) -> [list, list]:
    """
    The add_simple_noise_2d function is designed to introduce simple noise (random perturbations)
    to a given set of 2D points, where the noise is applied along either the x-axis or the y-axis

    :param W: W = [F0, X0] - given table function F(X). F0 = [F00, F01, ...]. X0 = [X00, X01, ...]
    :param axis: Ox or Oy - axis of deviation (see dict_directions)
    :param d: max deviation
    :return: F = [F0, F1, ...], X = [X0, X1, ...]. F(X) = F0(X0) + simple noise with even distribution
    """

    axis = dict_directions(axis)
    axis = int(not axis)
    FX = [copy.copy(W[0]), copy.copy(W[1])]

    for i in range(0, len(W[0])):
        FXsi = FX[axis][i]
        FX[axis][i] = even_distrib(FXsi - d, FXsi + d)
    F = FX[0]
    X = FX[1]

    return F, X


def add_simple_noise_example():

    A = [2, -3, -5, 7, -2, 8]
    F1, X1 = polynomial(A, a=-1, b=1, n=100)
    F2, X2 = add_simple_noise(W=[F1, X1], axis='y', d=2)

    S = {'F1': {'F': F1, 'X': X1, 'T': 'Line', 'Label': 'F(x)', 'Color': 'r', 'Line width': 1},
         'F2': {'F': F2, 'X': X2, 'T': 'Dots', 'Label': 'F(x) + Noise', 'Color': 'b', 'Line width': 1}}
    W = {'W1': {'S': S, 'ttl': 'Title', 'axisX': 'axisX1', 'axisY': 'axisY1'}}
    plot_sets_of_functions(W, False, True, False, 13)

    return
