import datetime
import matplotlib.pyplot as plt
from MathTools.log_files import check_log_folder


def plot_separate_functions_2d(M: list, ttl: list, input_type: int, key_save: bool, key_show: bool):
    """
    Description
        input_type = 0 means M = [F,X]. F = [F1, F2, ..., FN], Fi = [Fi1, Fi2, ..., FiJi] - ordinate points of function.
        Ji - number of points for Fi. X = [X1, ..., XN]. Xi = [Xi1, Xi2, ..., XiJi] - abscissa points Xij of function.

        input_type = 1 means M = [[F1,X1],[F2,X2], ... [FN,XN]], Fi = [Fi1, Fi2, ..., FiJi], Xi = [Xi1, Xi2, ..., XiJi].

    :param M: set of functions
    :param ttl: ttl = ['ttl1', 'ttl2', ... , 'ttlN'] - titles of functions Fi
    :param input_type: input_type = 0, 1 (see description)
    :param key_save: True/False - whether save or not
    :param key_show: True/False - whether show or not
    :return:
    """

    if key_save & key_show:
        print("plot_separate_functions. Cannot show and save at the same time")
    if input_type == 1:
        M = restructure_set_of_functions(M)
    if key_save:
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        N, P = check_log_folder()

    Height_of_picture = 13
    for i in range(0, len(M[0])):
        plt.figure(i, figsize=(Height_of_picture, 768 * Height_of_picture / 1366))  # for 1366 x 768 screen
        plt.title(ttl[i])
        plt.grid(which='major', fillstyle='left')
        plt.plot(M[1][i], M[0][i], color='b', linewidth=1, label=ttl[i])  # plot(X, F)
        if key_show:
            plt.show()
        if key_save:
            plt.savefig(
                'Data/Chapter ' + str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '/' + str(N) + '.' + str(
                    P + 1 + i) + '.png')

    return


def restructure_set_of_functions(Sf: list) -> list:
    """

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
