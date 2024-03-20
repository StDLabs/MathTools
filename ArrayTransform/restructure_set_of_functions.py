

def restructure_set_of_functions(Sf: list) -> list:
    """
    This function is responsible for restructuring the input data Sf into a list of lists containing the function
    values (F) and the corresponding domain values (X).

    :param Sf: Sf = [[F0, X0, Y0, ... ], [F1, X1, Y1, ... ], ... ] - set of N-dimensional functions.
               Fi = [fi0, fi1, ... ], Xi = [xi0, xi1, ... ], Yi = [yi0, yi1, ... ]
    :return: F = [F0, F1, ... ] - set of sets of destinations of functions.
             X = [X1, X2, ... ] - set of domains of functions.
             M = [F, X].
    """

    n = len(Sf[0]) - 1  # dimension
    F = []

    for i in range(0, len(Sf)):
        F.append(Sf[i][0])
    M = [F]
    for j in range(1, n + 1):
        Ms = []
        for i in range(0, len(Sf)):
            Ms.append(Sf[i][j])
        M.append(Ms)

    return M
