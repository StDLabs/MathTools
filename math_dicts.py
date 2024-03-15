from typing import Union


def dict_directions(axis: Union[str, int]) -> int:
    """

    :param axis: name or number of directions
    :return: i = 0, 1 or 2, 3 for Ox, Oy, Oz, Or
    """

    d: dict = {'x': 0, 'X': 0, 0: 0, 'Ox': 0,
               'y': 1, 'Y': 1, 1: 1, 'Oy': 1,
               'z': 2, 'Z': 2, 2: 2, 'Oz': 2,
               'r': 3, 'R': 3, 3: 3, 'Or': 3}
    axis = d[axis]

    return axis
