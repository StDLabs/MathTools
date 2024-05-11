import datetime
from MathTools.log_files import check_log_folder
from MathTools.ArrayTransform.Restructuring.transpose_vector_field import transpose_vector_field
import numpy as np
import copy
import matplotlib.pyplot as plt


def plot_vector_field_2d(G: list, input_type: int, relative: bool, key_save: bool, key_show: bool):
    """
    Description
        input_type = 0 means G = [R0, R1, ...] - set of vectors Ri = [Rix, Riy].

        input_type = 1 means G = [Gx, Gy], Gx = [R1x, R2x, ... ], Gy = [R1y, R2y, ...].

        input_type = 2 means G = [R0, R1, ...] - set of vectors Ri = [Rix0, Riy0, Rix, Riy].

        input_type = 3 means G = [X0, Y0, Gx, Gy], X0 = [R1x0, R2x0, ... ], Y0 = [R1y0, R2y0, ... ],
        Gx = [R1x, R2x, ... ], Gy = [R1y, R2y, ...]

    :param G:
    :param input_type: input_type = 0, 1, 2, 3 (see description)
    :param relative: relative = True/False - for input_type = 2 or 3 [Rix, Riy] can be determined either
    in the absolute system (False) or in the relative system (True) with the center in [Rix0, Riy0]
    :param key_save: True/False - whether save or not
    :param key_show: True/False - whether show or not
    :return:
    """

    if key_save & key_show:
        print("plot_vector_field_2d. Cannot show and save at the same time")

    if key_save:
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        N, P = check_log_folder()

    # converting all types to input_type = 3
    if input_type == 0:
        G = transpose_vector_field(G, True, True, 2)
    if input_type == 2:
        G = transpose_vector_field(G, False, True, 2)
    if input_type == 1:
        X0 = list(np.zeros(len(G[0])))
        Y0 = list(np.zeros(len(G[0])))
        G = [X0, Y0, G[0], G[1]]

    if (input_type == 0) | (input_type == 1):
        Gxs = copy.copy(G[2])
        Gxs.append(0)  # if you need to see the origin of the coordinate system
        Gys = copy.copy(G[3])
        Gys.append(0)  # if you need to see the origin of the coordinate system
    if (input_type == 2) | (input_type == 3):
        if not relative:
            Gxs = G[0] + G[2] + [0]
            Gys = G[1] + G[3] + [0]

            # plt.quiver plots only for relative x, y (G[2], G[3]).
            # In order to use absolute x, y it is necessary to add previous shift
            G[2] = [G[2][i] - G[0][i] for i in range(0, len(G[2]))]
            G[3] = [G[3][i] - G[1][i] for i in range(0, len(G[3]))]
        if relative:
            Ghx = list(np.array(G[2]) + np.array(G[0]))
            Ghy = list(np.array(G[3]) + np.array(G[1]))
            Gxs = G[0] + Ghx + [0]
            Gys = G[1] + Ghy + [0]

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

    plt.quiver(G[0], G[1], G[2], G[3], angles='xy', scale_units='xy', scale=1.0)
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
