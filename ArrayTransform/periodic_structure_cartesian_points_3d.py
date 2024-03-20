from MathTools.ArrayTransform.translate_set_of_vectors import translate_set_of_vectors


def periodic_structure_cartesian_points_3d(H: list, D: list, T: list, center: bool, Sh: list) -> list:
    """
    Description
        This function creates a list of cartesian points (vectors) with periodic symmetry

    :param H: H = [Hx, Hy, Hz] - quantity of nodal planes along x, y, z
    :param D: D = [Dxyx, Dxzx, Dyzy, Dyxy, Dzyz, Dzxz] - six quantities of shifts,
              where Dijk is a shift ij of plane ij along k
    :param T: T = [Tx, Ty, Tz] - three constant periods between nodal planes along x, y, z
    :param center: center = True/False - central symmetry of initial points or calculating coordinates from zeros
    :param Sh: Sh = [Sx, Sy, Sz] - parallel shift of all points along x, y, z
    :return: G = [R0, R1, R2, ...], Ri = [Rix, Riy, Riz] - set of points Ri with periodic structure
    """

    G = []
    for i in range(0, H[2]):
        for j in range(0, H[1]):
            for k in range(0, H[0]):
                G0 = k * T[0] + i * D[0] + j * D[1]
                G1 = j * T[1] + k * D[2] + i * D[3]
                G2 = i * T[2] + k * D[4] + j * D[5]
                G.append([G0, G1, G2])
    if center:
        for i in range(0, len(G)):
            G[i][0] += -T[0] * (H[0] - 1) / 2 - (H[2] - 1) * D[0] / 2 - (H[1] - 1) * D[1] / 2
            G[i][1] += -T[1] * (H[1] - 1) / 2 - (H[0] - 1) * D[2] / 2 - (H[2] - 1) * D[3] / 2
            G[i][2] += -T[2] * (H[2] - 1) / 2 - (H[0] - 1) * D[4] / 2 - (H[1] - 1) * D[5] / 2
    G = translate_set_of_vectors(G, Sh)

    return G
