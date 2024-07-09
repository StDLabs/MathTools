from MathTools.ArrayTransform.AnalytGeom.plane_type import plane_type
from MathTools.PointGenerators.SpatialFields.Central.point_charges_field_calc import point_charges_field_calc
import numpy as np


def scalar_field_section(Pl, P, Npl, G, Q, A, function):
    """
    Description
        This function calculates the scalar field values on a 2D rectangular grid section
        defined by a plane in 3D space, produced by sources connected to a set of points
        (for example, by a set of point charges).

        It supports calculations only for horizontal and vertical planes. Constructs a 2D grid based on user-defined
        nodal points and the area of interest. Evaluates the effect of point charges on the grid points using
        a user-defined field-producing function (for example classical Coulomb's field).

    :param Pl: Pl = [A, B, C, D] - parameters of a plane Ax+By+Cz+D=0 in space. The function supports calculations only
        for horizontal (parallel to the XY plane) and vertical planes (parallel to the XZ or YZ planes).
    :param P: P = [Px, Py, Pz] - defines the area bounds {{-Px,Px},{-Py,Py},{-Pz,Pz}} for calculations
    :param Npl: Npl = [N1, N2] - number of nodal points for 2D rectangular grid. This defines the grid resolution
    :param G: G = [R0, R1, R2, ...] - List of point charge locations Ri = [Rix, Riy, Riz]
    :param Q: Q = [Q0, Q1, Q2, ...], Qi - magnitudes point charges
    :param A: A = [A0, A1, A2, ...] - a list of all parameters needed for chosen type of the field producing function
    :param function: name of supported function (see point_charges_field_calc)
    :return: M1, M2, F
        M1 - the x-coordinates (or y, z depending on the plane orientation) of the 2D grid points along
        the first dimension
        M2 - the y-coordinates (or x, z depending on the plane orientation) of the 2D grid points along
        the second dimension.
        F - A 2D array representing the scalar field values at the grid points defined by M1 and M2.
    """

    plane_info = plane_type(Pl)
    if plane_info[2] == 2:
        s = plane_info[1][0]
        i1 = plane_info[3][0]
        i2 = plane_info[3][1]
        z = plane_info[3][2]
        U = -Pl[3] / Pl[s]
        h = [2 * P[i1] / Npl[1 - z], 2 * P[i2] / Npl[z]]
        M1 = [-P[i1] + j * h[0] for j in range(0, Npl[1 - z] + 1)]
        M2 = [-P[i2] + q * h[1] for q in range(0, Npl[z] + 1)]
        M = [0, 0, 0]
        M[s] = U
        F = np.zeros((Npl[z] + 1, Npl[1 - z] + 1))
        for j in range(0, Npl[1 - z] + 1):
            for q in range(0, Npl[z] + 1):
                M[i1] = M1[j]
                M[i2] = M2[q]
                F[q][j] = point_charges_field_calc(G, Q, M, A, function)
    else:
        print('point_charge_scalar_section: unsupported type of the plane Ax+By+Cz+D')

    return M1, M2, F
