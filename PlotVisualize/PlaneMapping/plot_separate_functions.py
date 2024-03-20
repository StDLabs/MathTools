import datetime
import matplotlib.pyplot as plt
from MathTools.log_files import check_log_folder
from MathTools.MultidimArrays.restructure_set_of_functions import restructure_set_of_functions
from MathTools.FunctionPoints.PlaneCurves.line_2d import line_2d


def plot_separate_functions(M: list, ttl: list, input_type: int, key_save: bool, key_show: bool):
    """
    This function is responsible for plotting a set of 2D functions and saving or displaying
    the plots based on the provided input. For each function in M, it creates a new figure, sets the title,
    adds a grid, and plots the function using matplotlib.

    :param M: A list containing the data points for the functions to be plotted
    :param ttl: ttl = ['ttl1', 'ttl2', ... , 'ttlN'] - A list of titles for the functions
    :param input_type: An integer value (0 or 1) indicating the format of the input data in M.
        input_type = 0 means M = [F,X]. F = [F1, F2, ..., FN], Fi = [Fi1, Fi2, ..., FiJi], Ji - number of points for Fi,
            X = [X1, ..., XN], Xi = [Xi1, Xi2, ..., XiJi]
        input_type = 1 means M = [[F1,X1],[F2,X2], ... [FN,XN]]. If input_type is 1, it calls
            the restructure_set_of_functions function to restructure the input data M.
    :param key_save: True/False - A boolean flag indicating whether to save the plots as image files. If key_save
        is True, it creates a folder based on the current date to save the plot images
    :param key_show: True/False - A boolean flag indicating whether to display the plots.
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


def plot_separate_functions_example():

    F1, X1 = line_2d(W=[3, -1], input_type=0, a=-5, b=5, n=50)
    F2, X2 = line_2d(W=[5, -2], input_type=0, a=-5, b=5, n=50)
    F3, X3 = line_2d(W=[[1, 2], [-3, -4]], input_type=1, a=-5, b=5, n=50)
    F4, X4 = line_2d(W=['x', -2], input_type=2, a=-5, b=5, n=50)
    F5, X5 = line_2d(W=['y', -3], input_type=2, a=-5, b=5, n=50)

    plot_separate_functions([[F1, X1], [F2, X2], [F3, X3], [F4, X4], [F5, X5]],
                            ['Title1', 'Title2', 'Title3', 'Title4', 'Title5'], 1, False, True)

    return
