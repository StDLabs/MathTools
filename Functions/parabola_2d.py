from MathTools.NumMethods.cramers_rule import cramers_rule


def parabola_2d(W: list, input_type: int, a: float, b: float, n: int) -> [list, list]:
    """

    :param W: list of all input parameters of parabola
    :param input_type: input_type = 0 means W = [A, B, C]  - parameters of parabola F = A*(X**2) + B*X + C.
                       input_type = 1 means W = [M0, M1, M2] - parabola that is uniquely determined
                                            by three points M0, M1, M2. M0 = [F0, X0], M1 = [F1, X1], M2 = [F2, X2].
    :param a: left boundary
    :param b: right boundary
    :param n: number of points
    :return: F = [F0, F1, ...], X = [X0, X1, ...] - points of parabola
    """

    if input_type == 1:
        M = []
        H = []
        for i in range(0, 3):
            Mi = []
            for j in range(0, 3):
                Mi.append(W[i][1] ** (2 - j))
            M.append(Mi)
            H.append(W[i][0])
        ABC = cramers_rule(M, H)
        W = ABC
    A = W[0]
    B = W[1]
    C = W[2]

    h = (b - a) / (n - 1)
    X = [a + h * i for i in range(0, n)]
    F = [A * (X[i] ** 2) + B * X[i] + C for i in range(0, n)]

    return F, X
