import numpy as np
from MathTools.math_dicts import dict_directions


def line_3d(W: list, input_type: int, n: int) -> [list, list, list]:
    """
    The line_3d function is designed to generate points on a 3D line based on different input types and parameters.
    Generates a set of points (x, y, z) that lie on a 3D line

    The function does not perform comprehensive input validation or error handling. It assumes
    that the input parameters are valid and within the expected ranges. The function does not handle cases where
    the input parameters might result in arithmetic errors or overflow conditions.

    :param W: A list containing the parameters that define the line. The interpretation of this list
        depends on the value of input_type
    :param input_type: input_type = 0 means W = [R0, M, t0, t1]. Parametric equations:
                                            x = x0 + a*t, y = y0 + b*t, z = z0 + c*t.
                                            t0, t1 - boundaries for parameter t. M = [a, b ,c] - collinear vector.
                                            R0 = [x0, y0, z0] - any point of the line.
                       input_type = 1 means W = [M0, M1] - Two points defining the line
                                            M0 = [x0, y0, z0], M1 = [x1, y1, z1].
                       input_type = 2 means W = [s, M, t0, t1]. s - name of axis Ox, Oy or Oz (see dict_directions).
                                            M = [Mx, My] or [Mx, Mz] or [My, Mz] - point on the surface
                                            Oxy, Oxz or Oyz where the line crosses it. a, b, N refer to the axis.
    :param n: number of points
    :return: X = [X0, X1, ...], Y = [Y0, Y1, ...], Z = [Z0, Z1, ...] - points of the line
    """

    if input_type == 0:
        R0 = W[0]
        M = W[1]
        t0 = W[2]
        t1 = W[3]
    if input_type == 1:
        R0 = W[0]
        M = list(np.array(W[1]) - np.array(W[0]))
        t0 = 0
        t1 = 1
    if input_type == 2:
        t0 = W[2]
        t1 = W[3]

    h = (t1 - t0) / (n - 1)
    t = [t0 + h * i for i in range(0, n)]

    if (input_type == 0) | (input_type == 1):
        R = []
        for i in range(0, 3):
            Ri = []
            for j in range(0, n):
                Ri.append(R0[i] + M[i] * t[j])
            R.append(Ri)
        X = R[0]
        Y = R[1]
        Z = R[2]

    if input_type == 2:
        s = dict_directions(W[0])
        S = t
        P1 = W[1][0] * np.ones(n)
        P2 = W[1][1] * np.ones(n)
        SP = [S, P1, P2]

        J = [[0, 1, 2],
             [1, 0, 2],
             [1, 2, 0]]
        Js = J[s]

        X = SP[Js[0]]
        Y = SP[Js[1]]
        Z = SP[Js[2]]

    return X, Y, Z
