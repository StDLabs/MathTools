import numpy as np
from MathTools.ArrayTransform.rotate_simple_3d_vector import rotate_simple_3d_vector


def rotate_3d_vector(R0: list, phi: float, axis, rotate_ini, relative: bool, r: list) -> list:
    """
    Rotates a 3D vector by a specified polar angle around a given axis, with the option to rotate around an initial
    point and handle relative or absolute coordinate systems.

    :param R0: R0 = [x0, y0, z0] or R0 = [x0_ini, y0_ini, z0_ini, x0, y0, z0] - given 3D vector
    :param phi: The polar angle (in radians) by which the vector should be rotated.
    :param axis: A string representing the axis of rotation. It can be one of the following:
        'X', 'Y', 'Z', or 'R' (for an arbitrary rotation axis).
    :param rotate_ini: If True, the initial point [x0_ini, y0_ini, z0_ini] will also be rotated.
    :param relative: If True, the rotation of [x0, y0, z0] is performed relative to the initial point
        [x0_ini, y0_ini, z0_ini]. If False, the rotation is performed in the absolute coordinate system.
    :param r: A list containing the components of the arbitrary rotation axis [rx, ry, rz].
        This parameter is required only if axis is 'R'.
    :return: R = [x, y, z] or R = [x_ini, x_ini, z_ini, x, y, z] - 3D vector R0 after rotation
    """

    n: bool = len(R0) == 6

    if n:
        R = [R0[3], R0[4], R0[5]]
        R_ini = [R0[0], R0[1], R0[2]]
    else:
        R = [R0[0], R0[1], R0[2]]

    if not n:
        R = rotate_simple_3d_vector(R, phi, axis, r)
    else:
        R = np.array(R)
        R_ini = np.array(R_ini)
        if not relative:
            R = np.array(rotate_simple_3d_vector(list(R - R_ini), phi, axis, r)) + R_ini
        else:
            R = np.array(rotate_simple_3d_vector(list(R), phi, axis, r))
        if rotate_ini:
            R_ini = np.array(rotate_simple_3d_vector(list(R_ini), phi, axis, r))
        R = list(R_ini) + list(R)

    return R
