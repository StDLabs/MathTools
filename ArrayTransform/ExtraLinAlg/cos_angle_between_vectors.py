import numpy as np


def cos_angle_between_vectors(A: list, B: list) -> float:
    """

    :param A: A = [ax, ay, az]
    :param B: B = [bx, by, bz]
    :return: cos_phi - cosine of angle between vectors
    """

    An = np.linalg.norm(A)
    Bn = np.linalg.norm(B)
    AB = np.dot(A, B)
    cos_phi = AB / (An * Bn)

    return cos_phi
