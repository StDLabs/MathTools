from MathTools.ArrayTransform.AnalytGeom.plane_type import plane_type
import numpy as np


def point_charge_scalar_section(Pl, P, Npl, function):
    """

    :param Pl: Pl = [A, B, C, D] - parameters of a plane Ax+By+Cz+D=0 in space
        (supports only horizontal and vertical planes)
    :param P: P = [Px, Py, Pz] - defines the area {{-Px,Px},{-Py,Py},{-Pz,Pz}} for calculations
    :param Npl: Npl = [N1, N2] - number of nodal points for 2D rectangular grid
    :return: GF =
    """
    plane_info = plane_type(Pl)
    if plane_info[2] == 2:
        s = plane_info[1][0]
        if s == 2:
            i2 = plane_info[0][0]
            i1 = plane_info[0][1]
            z = 0
        else:
            i1 = plane_info[0][0]
            i2 = plane_info[0][1]
            z = 1
        U = -Pl[3] / Pl[s]
        h = [2 * P[i1] / Npl[1 - z], 2 * P[i2] / Npl[z]]
        M1 = [-P[i1] + j * h[0] for j in range(0, Npl[1 - z] + 1)]
        M2 = [-P[i2] + q * h[1] for q in range(0, Npl[z] + 1)]
        M = [0, 0, 0]
        M[s] = U
        F = np.zeros((Npl[z] + 1, Npl[1 - z] + 1))
        for j in range(0, Npl[1 - z] + 1):
            for q in range(0, Npl[z] + 1):
                # print(j, q)
                M[i1] = M1[j]
                M[i2] = M2[q]
                if function == 'NAME':
                    F[q][j] = 1
    else:
        print('point_charge_scalar_section: unsupported type of the plane Ax+By+Cz+D')

    return GF
