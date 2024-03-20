import numpy as np
import math as m
from MathTools.math_dicts import dict_directions


def matrix_of_rotation_3d(phi: float, axis, r: list) -> np.array:
    """
    Generates the 3D rotation matrix for rotating vectors or points in a 3D space
    around a specified axis by a given polar angle

    :param phi: The polar angle (in radians) by which the rotation should be performed
    :param axis: A string representing the axis of rotation. It can be one of the following: 'X', 'Y', 'Z', or 'R'
        (for an arbitrary rotation axis).
    :param r: A list containing the components of the arbitrary rotation axis [rx, ry, rz].
    This parameter is required only if axis is 'R'.
    :return: M - Returns a NumPy array M representing the 3D rotation matrix corresponding
        to the specified axis and angle
    """

    cos_phi = m.cos(phi)
    sin_phi = m.sin(phi)
    axis = dict_directions(axis)

    if axis == 3:
        v_phi = 1 - cos_phi
        x = r[0]
        y = r[1]
        z = r[2]
        xxv = (x ** 2) * v_phi
        xyv = x * y * v_phi
        xzv = x * z * v_phi
        yyv = (y ** 2) * v_phi
        yzv = y * z * v_phi
        zzv = (z ** 2) * v_phi

    # 3D matrices of rotation around axes Ox, Oy, Oz, Or
    Mxyz = np.array([[[1, 0, 0],
                      [0, cos_phi, -sin_phi],
                      [0, sin_phi, cos_phi]],

                     [[cos_phi, 0, sin_phi],
                      [0, 1, 0],
                      [-sin_phi, 0, cos_phi]],

                     [[cos_phi, -sin_phi, 0],
                      [sin_phi, cos_phi, 0],
                      [0, 0, 1]],

                     [[xxv + cos_phi, xyv - z * sin_phi, xzv + y * sin_phi],
                      [xyv + z * sin_phi, yyv + cos_phi, yzv - x * sin_phi],
                      [xzv + y * sin_phi, yzv + x * sin_phi, zzv + cos_phi]]])
    M = Mxyz[axis]

    return M
