from MathTools.ArrayTransform.translate_set_of_vectors import translate_set_of_vectors


def periodic_structure_cartesian_points_2d(H: list, D: list, T: list, center: bool, Sh: list) -> list:
    """
    Description
        This function creates a list of cartesian points (vectors) with periodic symmetry

    :param H: H = [Hx, Hy] - quantity of nodal planes along x, y
    :param D: D = [Dx, Dy] - quantities of shifts of axes Ox and Oy
    :param T: T = [Tx, Ty] - three constant periods between nodal planes along x, y
    :param center: center = True/False - central symmetry of initial points or calculating coordinates from zeros
    :param Sh: Sh = [Sx, Sy] - parallel shift of all points along x, y
    :return: G = [R0, R1, R2, ...], Ri = [Rix, Riy] - set of points Ri with periodic structure
    """

    G = []
    for i in range(0, H[1]):
        for j in range(0, H[0]):
            G0 = j * T[0] + i * D[0]
            G1 = i * T[1] + j * D[1]
            G.append([G0, G1])
    if center:
        for i in range(0, len(G)):
            G[i][0] += -T[0] * (H[0] - 1) / 2 - (H[1] - 1) * D[0] / 2
            G[i][1] += -T[1] * (H[1] - 1) / 2 - (H[0] - 1) * D[1] / 2
    G = translate_set_of_vectors(G, Sh)

    return G
