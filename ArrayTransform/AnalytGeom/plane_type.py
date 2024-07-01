

def plane_type(P):
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
