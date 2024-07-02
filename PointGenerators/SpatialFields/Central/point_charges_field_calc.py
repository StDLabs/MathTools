import math as m
import numpy as np


def point_charges_field_calc(G, Q, M, A, function):
    """

    :param G: G = [R0, R1, R2, ...], Ri = [Rix, Riy, Riz] - set of points Ri where point charges are located
    :param Q: Q = [Q0, Q1, Q2, ...], Qi - magnitude of each point charge
    :param M: M = [Mx, My, Mz] - observation point
    :param A: A = [A0, A1, A2, ...] - a list of all parameters needed for chosen type of the field producing function
    :param function: name of supported function:
        1. function = 'hyperbola':
            A = [k, n]. Fi(r) = k*Qi/(r^n)
    :return: F = F(M)
    """

    F = 0
    for i in range(0, len(G)):
        r = m.sqrt(np.array([(G[i][j] - M[j])**2 for j in range(0, 3)]).sum())
        if function == 'hyperbola':
            # print(G[i], M)
            Fi = A[0] * Q[i] / (r ** A[1])
            F += Fi

    return F