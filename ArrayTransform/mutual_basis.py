from MathTools.ArrayTransform.scalar_triple_product import scalar_triple_product
import numpy as np
from MathTools.SetsSeriesSequences.alternating_series_for_number import alternating_series_for_number
from MathTools.SetsSeriesSequences.remove_number import remove_number


def mutual_basis(G: list) -> list:
    """

    :param G: initial basis G = [X, Y, Z]
    :return: Gn = [Xn, Yn, Zn] - mutual basis
    """

    Gn = []
    xyz = scalar_triple_product(G[0], G[1], G[2])
    o2 = alternating_series_for_number(3, 1)  # [1, -1, 1]
    for i in range(0, 3):
        o1 = remove_number(2, i)  # [1, 2], [0, 2], [1, 2]
        cross_i = np.cross(G[o1[0]], G[o1[1]])
        Gni = list(o2[i] * cross_i / xyz)
        Gn.append(Gni)

    return Gn
