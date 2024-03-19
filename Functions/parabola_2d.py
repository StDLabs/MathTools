from MathTools.NumMethods.cramers_rule import cramers_rule
from MathTools.PlotVisualize.plot_sets_of_functions_2d import plot_sets_of_functions_2d


def parabola_2d(W: list, input_type: int, a: float, b: float, n: int) -> [list, list]:
    """
    The function calculates the points of a 2D parabola based on either the provided coefficients or three points
    on the parabola, within the specified range and with the desired number of points

    :param W: list of all input parameters of parabola. A list containing either the coefficients of the parabola
        equation [A, B, C] or three points on the parabola [[F0, X0], [F1, X1], [F2, X2]]
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


def parabola_2d_example():
    F1, X1 = parabola_2d(W=[1, 2, 3], input_type=0, a=-4, b=3, n=100)
    F2, X2 = parabola_2d(W=[[8, -4], [-2, 0.5], [4, 2]], input_type=1, a=-4, b=3, n=100)

    S = {'F1': {'F': F1, 'X': X1, 'T': 'Dash', 'Label': 'W=[1, 2, 3]', 'Color': 'r', 'Line width': 1},
         'F2': {'F': F2, 'X': X2, 'T': 'Line', 'Label': 'W=[[8, -4], [-2, 0.5], [4, 2]', 'Color': 'b', 'Line width': 1.2},
         'F3': {'F': [8, -2, 4], 'X': [-4, 0.5, 2], 'T': 'Dots', 'Label': '[8, -4], [-2, 0.5], [4, 2]', 'Color': 'k', 'Line width': 1.5}}
    W = {'W1': {'S': S, 'ttl': 'Title', 'axisX': 'axisX1', 'axisY': 'axisY1'}}
    plot_sets_of_functions_2d(W, False, True, False, 13)

    return
