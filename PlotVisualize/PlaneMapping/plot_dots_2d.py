import datetime
from MathTools.log_files import check_log_folder
from MathTools.ArrayTransform.Restructuring.transpose_vector_field import transpose_vector_field
import copy
import matplotlib.pyplot as plt
import numpy as np
from MathTools.PointGenerators.PlaneCurves.line_2d import line_2d


def plot_dots(G: list, input_type: int, key_save: bool, key_show: bool):
    """
    The plot_dots_2d function plots a set of 2D vectors as dots on a Cartesian plane. It can handle two different
    input formats and provides options to save the plot as an image file or display it on the screen.

    :param G: set of 2d vectors
    :param input_type: input_type = 0, 1. An integer indicating the input format of G.
        input_type = 0 means G = [R0, R1, ...] - set of 2d vectors Ri = [Rix, Riy].
        input_type = 1 means G = [Gx, Gy], Gx = [R1x, R2x, ... ], Gy = [R1y, R2y, ...].
    :param key_save: A boolean flag indicating whether to save the plot as an image file or not.
    :param key_show: A boolean flag indicating whether to display the plot on the screen or not.
    :return:
    """

    if key_save & key_show:
        print("plot_dots_2d. Cannot show and save at the same time")

    if key_save:
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        N, P = check_log_folder()

    if input_type == 0:
        G = transpose_vector_field(G, False, False, 2)

    Gxs = copy.copy(G[0])
    Gxs.append(0)
    Gys = copy.copy(G[1])
    Gys.append(0)

    Xmin = min(Gxs)
    Xmax = max(Gxs)
    Ymin = min(Gys)
    Ymax = max(Gys)

    Height_of_picture = 13
    fig = plt.figure(1, figsize=(Height_of_picture, 768 * Height_of_picture / 1366))  # for 1366 x 768 screen
    ax = fig.add_subplot(111)

    # plot colored axes x, y
    C = ['b', 'g']  # colors for axes X, Y
    E = np.eye(2)  # matrix [[1, 0], [0, 1]]
    for i in range(0, 2):
        plt.quiver(0, 0, E[i][0], E[i][1], angles='xy', scale_units='xy', scale=1.0, color=C[i])
    for i in range(0, len(G[0])):
        plt.plot(G[0][i], G[1][i], 'ko')
    plt.axis([Xmin, Xmax, Ymin, Ymax])
    ax.set_aspect('equal', adjustable='box')
    plt.grid()

    if key_show:
        plt.show()
    if key_save:
        plt.savefig(
            'Data/Chapter ' + str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '/' + str(N) + '.' + str(
                P + 1) + '.png')

    return


def plot_dots_example():

    F1, X1 = line_2d(W=[3, -1], input_type=0, a=-5, b=5, n=50)
    F2, X2 = line_2d(W=[5, -2], input_type=0, a=-5, b=5, n=50)
    F3, X3 = line_2d(W=[[1, 2], [-3, -4]], input_type=1, a=-5, b=5, n=50)
    F4, X4 = line_2d(W=['x', -2], input_type=2, a=-5, b=5, n=50)
    F5, X5 = line_2d(W=['y', -3], input_type=2, a=-5, b=5, n=50)

    Gx = X1 + X2 + X3 + X4 + X5
    Gy = F1 + F2 + F3 + F4 + F5
    G = [Gx, Gy]
    plot_dots(G, input_type=1, key_save=False, key_show=True)

    return
