import random
import math as m
from scipy import special


def random_even_1d_distrib(a: float, b: float) -> float:
    """
    Generates a random floating-point number within a specified range with a uniform (even) distribution.

    :param a: left boundary
    :param b: right boundary
    :return: random x in [a, b] with even distribution
    """
    x = a + (b - a) * random.random()

    return x


def random_gauss_1d_distrib(sigma: float, mx: float) -> float:
    """
    Generates a random floating-point number following a Gaussian (normal) distribution with specified parameters.

    :param sigma: The standard deviation of the Gaussian distribution.
    :param mx: The mean (expectation) of the Gaussian distribution
    :return: random x with Gaussian distribution
    """

    x = sigma * m.sqrt(2) * special.erfinv(2 * random.random() - 1) + mx

    return x
