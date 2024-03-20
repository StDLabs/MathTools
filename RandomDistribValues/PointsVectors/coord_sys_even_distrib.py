from MathTools.RandomDistribValues.PointsVectors.vector_even_distrib import vector_even_distrib
import math as m


def coord_sys_even_distrib(M: list):
    """
    Generates a random coordinate system with an evenly distributed set of orthogonal unit vectors X, Y, and Z,
    originating from a specified point M.

    :param M: M = [x_ini, y_ini, z_ini] - origin of coordinate system
    :return: G = [X, Y, Z]. X = [Xx, Xy, Xz], Y = [Yx, Yy, Yz], Z = [Zx, Zy, Zz]
        A list containing the three orthogonal unit vectors X, Y, and Z, representing the new coordinate system.
        Each vector is represented as a list of its three components
    """

    X = vector_even_distrib(M, 1)
    Yx = M[0] - 1 / m.sqrt(1 + (X[0] / X[1]) ** 2)
    Yy = M[1] + 1 / m.sqrt(1 + (X[1] / X[0]) ** 2)
    Yz = M[2]
    Y = [M[0], M[1], M[2], Yx, Yy, Yz]
    Z = rotate_3d_vector(Y, m.pi / 2, 'Or', False, True, X)
    G = [X, Y, Y]

    return G
