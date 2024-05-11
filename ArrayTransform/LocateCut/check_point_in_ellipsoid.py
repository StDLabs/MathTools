import numpy as np


def check_point_in_ellipsoid(R: list, L: list) -> bool:
    """

    :param R: R = [x, y, z] - Any point in 3D Cartesian coordinate system
    :param L: L = [a, b, c] - Linear measures for an ellipsoid according to its canonical equation
    :return: key = True/False
    """

    key = (np.array([(R[j] / L[j]) ** 2 for j in range(0, 3)])).sum() <= 1
    if key:
        print('check_point_in_ellipsoid - False')

    return key
