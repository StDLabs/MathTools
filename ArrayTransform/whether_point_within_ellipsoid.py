import numpy as np


def whether_point_within_ellipsoid(R: list, L: list) -> bool:
    """

    :param R: R = [x, y, z] - some point
    :param L: L = [a, b, c] - parameters of ellipsoid a > b > c
    :return: True/False
    """

    key = (np.array([(R[j] / L[j]) ** 2 for j in range(0, 3)])).sum() <= 1
    if key:
        print('whether_point_within_ellipsoid - False')

    return key
