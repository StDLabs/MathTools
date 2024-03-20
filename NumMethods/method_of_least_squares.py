import numpy as np


def method_of_least_squares(W: list, rule) -> list:
    """
    Performs various types of regression analysis using the method of least squares.
    Supports linear, logarithmic, polynomial (with even and odd powers), and hyperbolic regression models

        rule = 0 means Linear regression with F = A1*x + A0. W = [F, X]. A = [A0, A1]

        rule = 1 means Logarithmic regression with F = A1*LnX + A0. W = [F, X]. A = [A0, A1]

        rule = 2 means Polynomial regression F = A0 + A1*x + A2*x**2 + A3*x**3 + ... AN*x**N).
        W = [F, X, N]. N - max power. A = [A0, A1, A2, ..., AN]

        rule = 3 means Polynomial regression with odd powers F = A0 + A1*x + A2*x**3 + A3*x**5 + ... AN*x**N.
        W = [F, X, N]. N - max power (must be an odd number). A = [A0, A1, A2, ..., A_((N+1)/2)]

        rule = 4 means Hyperbolic regression F = A1*X**(-N) + A0. W = [F, X, N].
        N - power of the hyperbola. A = [A0, A1]

        F = [F0, F1, ...], X = [X0, X1, ...]

    :param W: A list containing the necessary parameters for the regression analysis.
        The structure of W depends on the chosen rule (see rule)
    :param rule: rule = 0, 1, 2, 3 or 4

        rule = 0 means Linear regression with F = A1*x + A0. W = [F, X]. A = [A0, A1]

        rule = 1 means Logarithmic regression with F = A1*LnX + A0. W = [F, X]. A = [A0, A1]

        rule = 2 means Polynomial regression F = A0 + A1*x + A2*x**2 + A3*x**3 + ... AN*x**N).
        W = [F, X, N]. N - max power. A = [A0, A1, A2, ..., AN]

        rule = 3 means Polynomial regression with odd powers F = A0 + A1*x + A2*x**3 + A3*x**5 + ... AN*x**N.
        W = [F, X, N]. N - max power (must be an odd number). A = [A0, A1, A2, ..., A_((N+1)/2)]

        rule = 4 means Hyperbolic regression F = A1*X**(-N) + A0. W = [F, X, N].
        N - power of the hyperbola. A = [A0, A1]

        F = [F0, F1, ...], X = [X0, X1, ...]

    :return: Returns a list A containing the coefficients of the regression model, depending on the chosen rule.
        The order of coefficients in A corresponds to the powers of the independent variable in the regression equation.
    """

    L = len(W[0])
    F = np.array(W[0])
    X = np.array(W[1])

    if rule == 0:
        MXX = (X ** 2).sum()
        MX = X.sum()
        MF = F.sum()
        MXF = (X * F).sum()
        G = MXX * L - MX ** 2
        A1 = (MXF * L - MX * MF) / G
        A0 = (MXX * MF - MXF * MX) / G
        A = [A0, A1]

    if rule == 1:
        LnX = np.log(X)
        MXX = (LnX ** 2).sum()
        MX = LnX.sum()
        MF = F.sum()
        MXF = (F * LnX).sum()
        G = MXX * L - MX ** 2
        A1 = (MXF * L - MX * MF) / G
        A0 = (MXX * MF - MXF * MX) / G
        A = [A0, A1]

    if rule == 2:
        N = W[2]
        M = [[L]]

        for i in range(1, N + 1):
            M[0].append((X ** i).sum())

        for i in range(1, N + 1):
            Mi = []
            for j in range(0, N + 1):
                Mi.append((X ** (j + i)).sum())
            M.append(Mi)

        MF = [[F.sum()]]
        for i in range(1, N + 1):
            MF.append([(F * (X ** i)).sum()])
        M = np.array(M)
        MF = np.array(MF)
        A = np.linalg.solve(M, MF)
        A = np.transpose(A)
        A = list(A[0])

    if rule == 3:
        N = W[2]
        if (N + 1) % 2 != 0:
            print('method_of_least_squares.polynomial_regression: N must be an odd number')

        # MX1 = [Sum X, Sum X**3, Sum X**5, ..., Sum X**N] - sums for odd powers
        MX1 = []
        for i in range(1, int((N + 1) / 2) + 1):  # int is required only for changing type
            MX1.append((X ** (2 * i - 1)).sum())

        # MX2 = [Sum X**2, Sum X**4, ..., Sum X**2N] - sums for even powers
        MX2 = []
        for i in range(1, N + 1):
            MX2.append((X ** (2 * i)).sum())

        # MX22 = [[Sum X**2,     Sum X**4,     ..., Sum X**(N+1)],
        #         [Sum X**4,     Sum X**6,     ..., Sum X**(N+3)],
        #         [                      ...                    ],
        #         [Sum X**(N+1), Sum X**(N+3), ..., Sum X**2N   ]]
        MX22 = []
        for i in range(1, int((N + 1) / 2) + 1):
            MX22i = [MX2[j + i - 1] for j in range(0, int((N - 1) / 2) + 1)]
            MX22.append(MX22i)
        MX1T = np.transpose([MX1])  # transposed vector MX1

        # M = [[L,        Sum X,        Sum X**3,     ..., Sum X**N    ]
        #      [Sum X,    Sum X**2,     Sum X**4,     ..., Sum X**(N+1)],
        #      [Sum X**3, Sum X**4,     Sum X**6,     ..., Sum X**(N+3)],
        #      [                         ...                           ],
        #      [Sum X**N, Sum X**(N+1), Sum X**(N+3), ..., Sum X**2N   ]]

        K1 = np.hstack((MX1T, MX22))
        K2 = np.hstack(([[L]], [MX1]))
        M = np.vstack((K2, K1))

        # MF = [Sum F, Sum FX, Sum FX**3, ..., Sum FX**N]
        MF = [F.sum()]
        for i in range(1, int((N + 1) / 2) + 1):
            MF.append((F * (X ** (2 * i - 1))).sum())

        A = np.linalg.solve(M, MF)

    if rule == 4:
        N = W[2]
        XN = X**(-N)
        MX1 = XN.sum()
        MX2 = (XN**2).sum()
        MFX = [F.sum(), (F*XN).sum()]
        M = [[L,   MX1],
             [MX1, MX2]]
        A = np.linalg.solve(M, MFX)

    return A
