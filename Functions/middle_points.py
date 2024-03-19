

def middle_points(F: list, X: list) -> [list, list]:
    """
    The middle_points function is designed to extract the middle points from two input lists, F and X, assuming they
    represent evenly spaced points on a curve. This function returns set of all points with
    odd numbers from 0 to n (must be odd)

    :param F: F = [f0, f1, ...]
    :param X: X = [x0, x1, ...]
    :return: Fm = [ ..., fmi, ... ], Xm = [ ..., xmi, ... ], fmi = F(xmi), xmi = (x_(i+1) - x_i) / 2.
             This will work only with constant step
    """

    if (len(F) - 1) % 2 != 0 | (len(X) - 1) % 2 != 0:
        print("middle_points_of_function. n must be odd")
    Fm = [F[2 * i + 1] for i in range(0, int((len(F) - 1) / 2))]
    Xm = [X[2 * i + 1] for i in range(0, int((len(X) - 1) / 2))]

    return Fm, Xm
