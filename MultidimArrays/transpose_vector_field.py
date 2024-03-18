import numpy as np


def transpose_vector_field(G: list, ini0: bool, ini: bool, n: int) -> list:
    """
    The transpose_vector_field function transposes an N-dimensional vector field, which is represented
    as a list of vectors. It also provides options to add or remove initial points from the vectors.
    It transposes the list of vectors, effectively separating the coordinates and vector components
    into different lists. The transposed vector field can be useful in various applications, such as visualization,
    data analysis, and numerical simulations involving vector fields

    :param G: G = [R0, R1, ...] - A list of N-dimensional vectors, where each vector can be represented
        with or without an initial point.
        Ri = [x0i, y0i, ..., xi, yi, ... ] - i-th vector with an initial point.
        Ri = [xi, yi, ... ] - i-th vector without an initial point.
    :param ini0: A flag indicating whether to use zero initial points or not
    :param ini: A flag indicating whether to use initial points or not. If ini is False and the vectors in
        G have initial points, it removes the initial points from the vectors. If ini0 and ini are both True, it adds
        zero initial points to the vectors, even if they already have initial points
    :param n: The number of dimensions
    :return: G = [X0, Y0, ..., Gx, Gy, ... ] or G = [Gx, Gy, ...].
             X0 = [x00, x01, ... ], Y0 = [y00, y01, ... ], ... .
             Gx = [x0, x1, ... ], Gy = [y0, y1, ...], ... .
    """

    if (not ini) & (len(G[0]) == 2 * n):
        for i in range(0, len(G)):
            del G[i][0: n]
    if ini0 & ini:
        Z = list(np.zeros(n))
        if len(G[0]) == 2 * n:
            for i in range(0, len(G)):
                del G[i][0: n]
        for i in range(0, len(G)):
            G[i] = list(np.hstack(([Z], [G[i]]))[0])
    G = list(np.transpose(G))
    for i in range(0, len(G)):
        G[i] = list(G[i])

    return G
