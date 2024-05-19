import math as m
import numpy as np
from MathTools.ArrayTransform.Rotations.rotate_2d_vector import rotate_2d_vector
from MathTools.PlotVisualize.PlaneMapping.plot_dots_2d import plot_dots


def spiral_linear(R0, Rn, N, angle):
    """

    :param R0: initial radius (zero initial radius returns error)
    :param Rn: final radius
    :param N: number of points
    :param angle: whole angle of rotation
    :return:
    """

    A = [R0, 0]
    G = [A]
    phi = angle / N
    h = (Rn - R0) / N
    for i in range(0, N):
        Ar = rotate_2d_vector(G[i], phi, False, True)
        An = np.linalg.norm([Ar[0], Ar[1]])
        Ar = [Ar[0] * (1 + h / An), Ar[1] * (1 + h / An)]
        G.append(Ar)

    return G


def spiral_linear_example():

    R0 = 0.005
    Rn = 2
    N = 500
    angle = 10 * m.pi
    G = spiral_linear(R0, Rn, N, angle)
    plot_dots(G, input_type=0, key_save=False, key_show=True)

    return
