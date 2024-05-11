import numpy as np


def scalar_triple_product(A, B, C) -> float:
    """
    Consider the following order:
    ((AxB),C)

    :param A: A = [ax, ay, az]
    :param B: B = [bx, by, bz]
    :param C: C = [cx, cy, cz]
    :return: V
    """

    V = np.dot(np.cross(A, B), C)

    return V
