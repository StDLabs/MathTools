import numpy as np


def direction_cosines(A) -> list:
    """

    :param A: A = [Ax, Ay, Az] - 3D vector
              or A = [x, y, z, Ax, Ay, Az] - 3D vector in an observation point
    :return: d_cosines = [cos1, cos2, cos3] - direction cosines for vector A = [Ax, Ay, Az]
    """

    if len(A) == 6:
        A = [A[3], A[4], A[5]]
    if len(A) == 3:
        An = np.linalg.norm(A)
        d_cosines = [A[i] / An for i in range(0, 3)]

    return d_cosines
