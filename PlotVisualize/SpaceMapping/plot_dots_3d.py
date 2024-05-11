import datetime
from MathTools.log_files import check_log_folder
from MathTools.ArrayTransform.Restructuring.transpose_vector_field import transpose_vector_field
import matplotlib.pyplot as plt
import numpy as np


def plot_dots_3d(G: list, input_type, key_save, key_show):
    """
    Description
        input_type = 0 means G = [R0, R1, ...] - set of vectors Ri = [Rix, Riy, Riz].

        input_type = 1 means G = [Gx, Gy, Gz], Gx = [R1x, R2x, ... ], Gy = [R1y, R2y, ...], Gz = [R1y, R2y, ...].

    :param G: set of 3d vectors
    :param input_type: input_type = 0, 1 (see description)
    :param key_save: True/False - whether save or not
    :param key_show: True/False - whether show or not
    :return:
    """

    if key_save & key_show:
        print("plot_dots_3d. Cannot show and save at the same time")

    if key_save:
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        N, P = check_log_folder()

    if input_type == 0:
        G = transpose_vector_field(G, False, False, 3)

    Gs = G[0] + G[1] + G[2] + [0]
    Smin = min(Gs)
    Smax = max(Gs)

    Height_of_picture = 13
    fig = plt.figure(1, figsize=(Height_of_picture, 768 * Height_of_picture / 1366))  # for 1366 x 768 screen
    ax = fig.add_subplot(111, projection='3d')

    # plot colored axes x, y, z
    E = np.eye(3)  # matrix [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    C = ['b', 'g', 'r']  # colors for axes X, Y, Z
    for i in range(0, 3):
        plt.quiver(0, 0, 0, E[i][0], E[i][1], E[i][2], arrow_length_ratio=0.1, colors=C[i])

    for i in range(0, len(G[0])):
        plt.plot(G[0][i], G[1][i], G[2][i], 'ko')
    ax.set_xlim(Smin, Smax)
    ax.set_ylim(Smin, Smax)
    ax.set_zlim(Smin, Smax)
    ax.set_aspect('auto', adjustable='box')
    plt.grid()

    if key_show:
        plt.show()
    if key_save:
        plt.savefig(
            'Data/Chapter ' + str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '/' + str(N) + '.' + str(
                P + 1) + '.png')

    return
