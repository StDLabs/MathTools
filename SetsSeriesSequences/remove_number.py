

def remove_number(n: int, x: int) -> list:
    """

    :param n: n - last number in the set [0, 1, 2, 3, ..., n]
    :param x: number that you need to remove
    :return: o = [0, 1, 2, ... x-1, x+1, ..., n]
    """

    o = [i for i in range(0, n + 1)]
    del o[x: x + 1]

    return o
