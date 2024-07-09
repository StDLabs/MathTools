from MathTools.PointGenerators.SpatialFields.Central.point_charges_field_calc import point_charges_field_calc
import numpy as np


def scalar_field_3d(P, N3d, G, Q, A, function):
    """
    Description
        Computes a 3D scalar field due to a set of point charges.
        Generates a mesh grid and calculates field values at each grid point

    :param P: P = [Px, Py, Pz] - defines the area bounds {{-Px,Px},{-Py,Py},{-Pz,Pz}} for calculations
    :param N3d: N3d = [N1, N2, N3] - number of nodal points for 3D rectangular grid. This defines the grid resolution
    :param G: G = [R0, R1, R2, ...] - List of point charge locations Ri = [Rix, Riy, Riz]
    :param Q: Q = [Q0, Q1, Q2, ...], Qi - magnitudes point charges
    :param A: A = [A0, A1, A2, ...] - a list of all parameters needed for chosen type of the field producing function
    :param function: name of supported function (see point_charges_field_calc)
    :return:
    """

    h = [2 * P[i] / N3d[i] for i in range(0, 3)]
    M = [0, 0, 0]
    for i in range(0, 3):
        M[i] = [-P[i] + j * h[i] for j in range(0, N3d[i] + 1)]
    M = np.array(M)
    MQ = np.zeros((N3d[0] + 1, N3d[1] + 1, N3d[2] + 1))
    for i in range(0, N3d[0] + 1):
        for j in range(0, N3d[1] + 1):
            for q in range(0, N3d[2] + 1):
                Mijq = [M[0][i], M[1][j], M[2][q]]
                MQ[i][j][q] = point_charges_field_calc(G, Q, Mijq, A, function)

    return M, MQ
