from MathTools.RandomDistribValues.PointsVectors.rotation_even_distrib import rotation_even_distrib
import math as m


def vector_even_distrib(M: list, r: float) -> list:
    """

    :param r: length of vector
    :param M: M = [x_ini, y_ini, z_ini] - initial point of vector
    :return: R = [x_ini, y_ini, z_ini, x, y, z] - random vector with even distribution over sphere
    """

    phi, cos_t, sin_t = rotation_even_distrib()
    sin_phi = m.sin(phi)
    cos_phi = m.cos(phi)
    rx = r * sin_t * cos_phi
    ry = r * sin_t * sin_phi
    rz = r * cos_t
    R = [rx, ry, rz]
    R = M + R

    return R
