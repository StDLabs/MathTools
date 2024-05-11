

def part_of_set(G: list, M: list, n: int) -> list:
    """
    Description
        G can be represented as G = G0 + G1 + G2 + ... + GN (n = 0, 1, 2, ..., N).
        Each set Gn consists of Mn vectors Rmn = [x_mn, y_mn, z_mn]. Gn = [R0n, R1n, ..., RMn].
        M = [M0, M1, ..., Mn] where Mn - number of vectors for each Gn.
        This function returns Gn = [R0n, R1n, ..., RMn] by number n.


    :param G: G = [R0, R1, ... ] - set of vectors Ri = [xi, yi, ... ]
    :param M: M = [M0, M1, ..., Mn] - set of numbers of vectors for each Gn
    :param n: n = 0, 1, 2, ... - number of set
    :return: Gn = [R0n, R1n, ..., RMn]
    """

    s = 0
    Gn = []
    for i in range(0, n):
        s += M[i]
    for i in range(s, s + M[n]):
        Gn.append(G[i])

    return Gn
