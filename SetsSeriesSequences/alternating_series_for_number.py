

def alternating_series_for_number(n: int, x0) -> list:
    """

    :param n: n - number of elements in series [x0, -x0, x0, -x0, x0, ... ]
    :param x0: x0 - first element
    :return: o
    """

    o = [x0 * ((-1) ** i) for i in range(0, n)]

    return o
