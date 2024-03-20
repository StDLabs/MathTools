

def translate_set_of_vectors(G: list, Sh: list) -> list:
    """
    Translates a set of vectors or points in a given dimensional space by specified
    translation values along each coordinate axis

    :param G: G = [R0, R1, ... ] - A list of vectors or points, where each element is a list representing
        the coordinates of a vector or point. The structure is G = [R0, R1, ...],
        where Ri = [xi, yi, ...] represents the coordinates of the i-th vector or point.
    :param Sh: Sh = [Sx, Sy, ... ] - A list containing the translation values for each coordinate axis,
        in the format Sh = [Sx, Sy, ...], where Sx is the translation value along the x-axis,
        Sy is the translation value along the y-axis, and so on
    :return: G = [R0, R1, ...] - Returns a list Gsh containing the translated vectors or points.
        The structure of Gsh is the same as G, but with the coordinates of each vector or point translated by the
        corresponding values in Sh.
    """

    n = len(G[0])  # dimension
    Gsh = []

    for i in range(0, len(G)):
        Gsh.append([])
        for j in range(0, n):
            Gsh[i].append(G[i][j] + Sh[j])

    return Gsh
