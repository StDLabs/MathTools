import math as m
from MathTools.NumMethods.numerical_integration import numerical_integration


def elliptical_integral(L: list, ksi: float, n: int) -> float:
    """

    :param L: L = [a, b, c] - parameters of ellipsoid a > b > c
    :param ksi: ellipsoidal coordinate
    :param n: number of points
    """

    phi_0 = m.asin(m.sqrt((L[0] ** 2 - L[2] ** 2)/(L[0] ** 2 + ksi)))
    h = phi_0 / (n - 1)
    k1 = (L[0] ** 2 - L[1] ** 2) / (L[0] ** 2 - L[2] ** 2)
    k2 = 2 * (1 / m.sqrt((L[0] ** 2 - L[2] ** 2) ** 3))

    phi = [i * h for i in range(0, n)]
    F = [1 / m.sqrt(1 - k1 * (m.sin(phi[i]) ** 2)) for i in range(0, n)]

    value = k2 * numerical_integration(F, [], phi, 0, phi_0, 'simpson', 'constant')

    return value
