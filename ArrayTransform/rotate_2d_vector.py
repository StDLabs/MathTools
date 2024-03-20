import numpy as np
from MathTools.ArrayTransform.rotate_simple_2d_vector import rotate_simple_2d_vector


def rotate_2d_vector(R0: list, phi: float, rotate_ini: bool, relative: bool) -> list:
    """
    Rotates a 2D vector by a specified polar angle, with the option to rotate around an initial point
    and handle relative or absolute coordinate systems

    :param R0: A list representing the initial 2D vector. It can have two formats:
        R0 = [x0, y0] (Coordinates of the vector) or
        R0 = [x0_ini, y0_ini, x0, y0] (Coordinates of the initial point and the vector)
    :param phi: phi - The polar angle (in radians) by which the vector should be rotated
    :param rotate_ini: If True, the initial point [x0_ini, y0_ini] will also be rotated
    :param relative: If True, the rotation of [x0, y0] is performed relative to the initial point [x0_ini, y0_ini].
        If False, the rotation is performed in the absolute coordinate system
    :return: R representing the rotated 2D vector. The format of R depends on the input format of R0.
        R = [x, y] or R = [x_ini, x_ini, x, y]
    """

    n: bool = len(R0) == 4

    if n:
        R = [R0[2], R0[3]]
        R_ini = [R0[0], R0[1]]
    else:
        R = [R0[0], R0[1]]

    if not n:
        R = rotate_simple_2d_vector(R, phi)
    else:
        R = np.array(R)
        R_ini = np.array(R_ini)
        if not relative:
            R = np.array(rotate_simple_2d_vector(list(R - R_ini), phi)) + R_ini
        else:
            R = np.array(rotate_simple_2d_vector(list(R), phi))
        if rotate_ini:
            R_ini = np.array(rotate_simple_2d_vector(list(R_ini), phi))
        R = list(R_ini) + list(R)

    return R
