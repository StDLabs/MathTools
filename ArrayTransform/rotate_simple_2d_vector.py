import math as m
import numpy as np


def rotate_simple_2d_vector(R0: list, phi: float) -> list:
    """
    Performs a 2D rotation of a vector by a specified angle (polar angle) in a 2D plane

    :param R0: R0 = [x0, y0] - A list containing the coordinates of the initial 2D vector, in the format [x0, y0].
    :param phi: phi - The polar angle (in radians) by which the vector should be rotated in the 2D plane.
    :return: Returns a list R = [x, y] containing the coordinates of the rotated 2D vector, in the format [x, y].
    """

    R0 = np.array(R0)

    CosPhi = m.cos(phi)
    SinPhi = m.sin(phi)
    M = np.array([[CosPhi, -SinPhi], [SinPhi, CosPhi]])  # 2D matrix of rotation

    R = list(np.matmul(M, R0))

    return R
