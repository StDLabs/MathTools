import math as m
import random


def rotation_even_distrib():
    """
    Generates a set of three random values representing the angle phi
    and the cosine and sine values (cos_t and sin_t) for a uniform distribution of points on a unit sphere.
    The rotation_even_distrib function is designed to generate random values that can be used to distribute points
    evenly on the surface of a unit sphere. This is useful in various applications, such as 3D modeling,
    computer graphics, and simulations involving spherical geometry.

        phi - a random angle value within the range [0, 2π).

        cos_t - A random cosine value within the range [-1, 1]

        sin_t - A random sine value within the range [-1, 1], calculated based on the generated cos_t value
            to ensure that cos_t^2 + sin_t^2 = 1

    :return: phi, cos_t, sin_t
    """

    ops1 = random.random()
    ops2 = random.random()
    ops3 = (-1) ** round(random.random())
    phi = 2 * m.pi * ops1
    cos_t = 1 - 2 * ops2
    sin_t = ops3 * m.sqrt(1 - cos_t ** 2)

    return phi, cos_t, sin_t
