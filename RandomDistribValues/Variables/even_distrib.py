import random


def even_distrib(a: float, b: float) -> float:
    """
    Generates a random floating-point number within a specified range with a uniform (even) distribution.

    :param a: left boundary
    :param b: right boundary
    :return: random x in [a, b] with even distribution
    """
    x = a + (b - a) * random.random()

    return x
