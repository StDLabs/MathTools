import numpy as np

def direction_cosines(A) -> list:
    """

    :param A: A = [x, y, z] or A = [x_ini, y_ini, z_ini, x, y, z]
    :return: d_cosines = [cos_1, cos_2, cos_3]
    """

    if len(A) == 6:
        A = [A[3], A[4], A[5]]
    if len(A) == 3:
        An = np.linalg.norm(A)
        d_cosines = [A[i] / An for i in range(0, 3)]

    return d_cosines
