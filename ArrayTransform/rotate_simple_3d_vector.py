import numpy as np
from MathTools.ArrayTransform.matrix_of_rotation_3d import matrix_of_rotation_3d


def rotate_simple_3d_vector(R0: list, phi: float, axis, r: list) -> list:
    """
    Rotates a 3D vector by a specified polar angle around a given axis in a 3D space

    :param R0: R0 = [x0, y0, z0] or R0 = [x0_ini, y0_ini, z0_ini, x0, y0, z0] - given 3D vector
    :param phi: The polar angle (in radians) by which the vector should be rotated
    :param axis: A string representing the axis of rotation. It can be one of the following:
        'X', 'Y', 'Z', or 'R' (for an arbitrary rotation axis).
    :param r: A list containing the components of the arbitrary rotation axis [rx, ry, rz].
        This parameter is required only if axis is 'R'.
    :return: R = [x, y, z] or R = [x_ini, x_ini, z_ini, x, y, z] - 3D vector R0 after rotation
    """

    R0 = np.array(R0)
    M = matrix_of_rotation_3d(phi, axis, r)
    R = list(np.matmul(M, R0))

    return R
