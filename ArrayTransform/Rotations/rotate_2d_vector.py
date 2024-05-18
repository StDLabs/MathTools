import numpy as np
import math as m
from MathTools.ArrayTransform.Rotations.rotate_simple_2d_vector import rotate_simple_2d_vector
from MathTools.PlotVisualize.PlaneMapping.plot_vector_field_2d import plot_vector_field_2d


def rotate_2d_vector(A: list, phi: float, rotate_rad: bool, relative: bool) -> list:
    """
    Rotates a 2D vector by a specified polar angle, with the option to rotate around an initial point
    and handle relative or absolute coordinate systems

    :param A: A list representing the initial 2D vector. It can have two formats:
        A = [Ax, Ay] (vector projections) or
        A(R) = [x, y, Ax, Ay] (Coordinates of an observation point R = [x, y] (radius-vector)
        and vector projections A = [Ax, Ay] (main vector value))
    :param phi: phi - The polar angle (in radians) by which the vector is to be rotated
    :param rotate_rad: If True, the radius-vector R = [x, y] will also be rotated around z-axis
    :param relative: If True, the rotation of the main vector A = [Ax, Ay] is performed relatively
        to the observation point R = [x, y]. If False, the rotation is performed in the absolute coordinate system
    :return: Ar representing the rotated 2D vector. The format of Ar depends on the input format of A.
        Ar = [Arx, Ary] or Ar(Rr) = [xr, yr, Arx, Ary]
    """

    n: bool = len(A) == 4

    if n:
        Ar = [A[2], A[3]]
        R = [A[0], A[1]]
    else:
        Ar = [A[0], A[1]]

    if not n:
        Ar = rotate_simple_2d_vector(Ar, phi)
    else:
        Ar = np.array(Ar)
        R = np.array(R)
        if not relative:
            Ar = np.array(rotate_simple_2d_vector(list(Ar - R), phi)) + R
        else:
            Ar = np.array(rotate_simple_2d_vector(list(Ar), phi))
        if rotate_rad:
            R = np.array(rotate_simple_2d_vector(list(R), phi))
        Ar = list(R) + list(Ar)

    return Ar


def rotate_2d_vector_example():

    R = [2, 2]
    A = [-0.65, 0.75]
    G = [[R[0], R[1], A[0], A[1]]]
    N = 100
    An = np.linalg.norm(A)
    h = An / N
    phi = m.pi / (N / 2)
    for i in range(0, N):
        Ar = rotate_2d_vector(G[i], phi, False, True)
        An = np.linalg.norm([Ar[2], Ar[3]])
        Ar = [Ar[0], Ar[1], Ar[2] * (1 + h / An), Ar[3] * (1 + h / An)]
        G.append(Ar)
    plot_vector_field_2d(G, 2, True, False, True)

    return
