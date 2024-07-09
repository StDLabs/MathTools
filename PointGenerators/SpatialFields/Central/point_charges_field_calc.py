from MathTools.ArrayTransform.ExtraLinAlg.direction_cosines import direction_cosines
import math as m
import numpy as np


def point_charges_field_calc(G, Q, M, A, function, option):
    """

    :param G: G = [R0, R1, R2, ...], Ri = [Rix, Riy, Riz] - set of points Ri where point charges are located
    :param Q: Q = [Q0, Q1, Q2, ...], Qi - magnitude of each point charge
    :param M: M = [Mx, My, Mz] - observation point
    :param A: A = [A0, A1, A2, ...] - a list of all parameters needed for chosen type of the field producing function
    :param function: name of supported function:
        1. function = 'hyperbola':
            A = [k, n, Rm, Fm]. Fi(r) = k*Qi/(r^n) if r > Rm; Fi(r) = Fm if r <= Rm
    :param option: choice of 'scalar' or 'vector' filed
    :return: F = F(M)
    """

    F = {'scalar': 0, 'vector': np.array([0, 0, 0])}
    for i in range(0, len(G)):
        r_vec = np.array([(M[j] - G[i][j]) for j in range(0, 3)])
        r = m.sqrt((r_vec ** 2).sum())
        if function == 'hyperbola':
            Fi = A[3] if r <= A[2] else A[0] * Q[i] / (r ** A[1])
            if option == 'vector':
                d_cos = np.array(direction_cosines(r_vec.tolist()))
                Fi = d_cos * Fi
            F[option] = F[option] + Fi
    if option == 'vector':
        F[option].tolist()

    return F[option]
