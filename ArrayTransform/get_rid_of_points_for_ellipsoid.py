import numpy as np


def get_rid_of_points_for_ellipsoid(M: list, G: list, L: list, where: str) -> list:
    """

    :param M: center of ellipsoid
    :param G: set of points (vectors)
    :param L: L = [a, b, c] parameters of ellipsoid
    :param where: where = 'outside'/'inside' means getting rid of points outside/inside the ellipsoid
    :return: Gn - set of points (vectors)
    """

    Gn = []
    for i in range(0, len(G)):
        p = np.array([((M[s] - G[i][s]) / L[s]) ** 2 for s in range(0, 3)]).sum()
        if where == 'outside':
            if p <= 1:
                Gn.append(G[i])
        if where == 'inside':
            if p >= 1:
                Gn.append(G[i])

    return Gn
