

def plane_type(P):
    """
    A, B, C, D can be zero parameters. Function returns positions of zero parameters K1,
    positions of non-zero parameters K2, and the type of plane T:
    T = 0 (no zero parameters), T = 1 (one zero parameter), or 2 (two zero parameters)

    :param P: P = [A, B, C, D] - parameters of a plane Ax+By+Cz+D=0 in space
    :return: S = [K1, K2, T]
    """

    type = 0
    i = 0
    K1 = []
    K2 = []
    S = []
    while i <= 2:
        if P[i] == 0:
            K1.append(i)
            type += 1
        else:
            K2.append(i)
        i += 1
    S.append(K1)
    S.append(K2)
    S.append(type)
    return S
