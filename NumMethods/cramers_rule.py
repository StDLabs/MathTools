import numpy as np
import copy


def cramers_rule(A: list, B: list) -> list:
    """
    The provided code implements Cramer's Rule, which is a method for solving systems of linear equations.
    The function returns a list X containing the solutions to the system of linear equations.
    Cramer's Rule provides a way to solve systems of linear equations by computing determinants of matrices formed
    by replacing columns of the coefficient matrix with the constant terms. It is particularly useful for small systems
    of equations but can be computationally expensive for larger systems

        There's a system of linear equations:

        a00*x0 + a01*x1 + ... + a0n*xn = b0

        ...

        an1*x0 + an1*x1 + ... + ann*xn = bn

    :param A: A = [[a00, a01, ... ], [a10, a11, ... ], ..., [an0, an1, ... ]] - A list representing the coefficient
        matrix of the system of linear equations
    :param B: B = [b0, b1, ..., bn] - A list representing the constant terms (right-hand side) of the system
    :return: X = [x0, x1, ..., xn] - vector of solutions
    """

    A = np.array(A)
    B = np.array(B)

    D = []
    for i in range(0, len(A[0])):
        Di = copy.copy(A)
        Di[:, i] = B
        Di = np.linalg.det(Di)
        D.append(Di)

    W = np.linalg.det(A)

    X = []
    for i in range(0, len(A[0])):
        X.append(D[i] / W)

    return X
