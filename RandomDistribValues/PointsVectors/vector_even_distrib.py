from MathTools.RandomDistribValues.PointsVectors.rotation_even_distrib import rotation_even_distrib
import math as m


def vector_even_distrib(M: list, r: float) -> list:
    """
    Generates a random vector with a specified length r, originating from a given point M, and with an evenly
    distributed direction on a sphere

    :param r: The desired length of the random vector
    :param M: M = [x_ini, y_ini, z_ini] - initial point of vector
    :return: R = [x_ini, y_ini, z_ini, x, y, z] - Its direction is randomly distributed on a sphere, ensuring
        an even distribution of vectors on the spherical surface
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
