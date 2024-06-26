import math as m
from MathTools.ArrayTransform.Rotations.rotate_2d_vector import rotate_2d_vector
from MathTools.PlotVisualize.PlaneMapping.plot_dots_2d import plot_dots


def circle(R, N):
    """

    :param R: R - circle radius
    :param N: N - number of points of the whole circle (even distribution)
    :return: G = [R0, R1, ... ], Ri = [Rix, Riy] - points of the circle
    """

    A = [R, 0]
    G = [A]
    phi = 2 * m.pi / N
    for i in range(0, N):
        Ar = rotate_2d_vector(G[i], phi, False, True)
        G.append(Ar)

    return G


def circle_example():

    R = 2
    N = 50
    G = circle(R, N)
    plot_dots(G, input_type=0, key_save=False, key_show=True)

    return
