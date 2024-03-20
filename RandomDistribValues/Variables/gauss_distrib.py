import random
import math as m
from scipy import special


def gauss_distrib(sigma: float, mx: float) -> float:
    """
    Generates a random floating-point number following a Gaussian (normal) distribution with specified parameters.

    :param sigma: The standard deviation of the Gaussian distribution.
    :param mx: The mean (expectation) of the Gaussian distribution
    :return: random x with Gaussian distribution
    """

    x = sigma * m.sqrt(2) * special.erfinv(2 * random.random() - 1) + mx

    return x
