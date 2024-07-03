

def plane_type(Pl):
    """
    Parameters A, B, C (positions 0, 1, 2) of a plane Ax+By+Cz+D=0 in space can be zero parameters.
    Function returns positions (0, 1 or 2) of zero parameters K1, positions (0, 1 or 2) of non-zero parameters K2,
    the type of plane T: T = 0 (no zero parameters), T = 1 (one zero parameter), or 2 (two zero parameters),
    and axes order XYZ

    :param Pl: Pl = [A, B, C, D] - parameters of a plane Ax+By+Cz+D=0 in space
    :return: S = [K1, K2, T, XYZ]
    """

    type = 0
    i = 0
    K1 = []
    K2 = []
    S = []
    while i <= 2:
        if Pl[i] == 0:
            K1.append(i)
            type += 1
        else:
            K2.append(i)
        i += 1

    S.append(K1)
    S.append(K2)
    S.append(type)

    if S[2] == 2:
        if S[1][0] == 2:
            i2 = S[0][0]
            i1 = S[0][1]
            z = 0
        else:
            i1 = S[0][0]
            i2 = S[0][1]
            z = 1

        S.append([i1, i2, z])

    return S
