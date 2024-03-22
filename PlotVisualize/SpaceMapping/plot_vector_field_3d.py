import datetime
from MathTools.log_files import check_log_folder
import matplotlib.pyplot as plt
from MathTools.ArrayTransform.transpose_vector_field import transpose_vector_field
import numpy as np


def plot_vector_field_3d(G: list, input_type: int, relative: bool, key_save: bool, key_show: bool):
    """
    Description
        input_type = 0 means G = [R0, R1, ...] - set of vectors, Ri = [Rix, Riy, Riz].

        input_type = 1 means G = [Gx, Gy, Gz], Gx = [R1x, R2x, ... ], Gy = [R1y, R2y, ...], Gz = [R1y, R2y, ...]

        input_type = 2 means G = [R0, R1, ...] - set of vectors Ri = [Rix0, Riy0, Riz0, Rix, Riy, Riz]

        input_type = 3 means G = [X0, Y0, Z0, Gx, Gy, Gz], X0 = [R1x0, R2x0, ... ], Y0 = [R1y0, R2y0, ... ],
        Z0 = [R1z0, R2z0, ...], Gx = [R1x, R2x, ... ], Gy = [R1y, R2y, ...], Gz = [R1z, R2z, ...]

    :param G:
    :param input_type: input_type = 0, 1, 2, 3
    :param relative: relative = True/False - for input_type = 2 or 3 [Rix, Riy, Riz] can be determined either
    in the absolute system (False) or in the relative system (True) with the center in [Rix0, Riy0, Riz0]
    :param key_save: True/False - whether save or not
    :param key_show: True/False - whether show or not
    :return:
    """

    if key_save & key_show:
        print("plot_vector_field_3d. Cannot show and save at the same time")

    if key_save:
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        N, P = check_log_folder()

    # converting all types to input_type = 3
    if input_type == 0:
        G = transpose_vector_field(G, True, True, 3)
    if input_type == 2:
        G = transpose_vector_field(G, False, True, 3)
    if input_type == 1:
        X0 = list(np.zeros(len(G[0])))
        Y0 = list(np.zeros(len(G[0])))
        Z0 = list(np.zeros(len(G[0])))
        G = [X0, Y0, Z0, G[0], G[1], G[2]]

    if (input_type == 0) | (input_type == 1):
        Gs = []
        for i in range(0, 3):
            Gs += G[3 + i]
        Gs.append(0)  # if you need to see the origin of the coordinate system
    if (input_type == 2) | (input_type == 3):
        if not relative:
            Gs = []
            for i in range(0, 6):
                Gs += G[i]

            # plt.quiver plots only for relative x, y, z (G[3], G[4], G[5]).
            # In order to use absolute x, y, z it is necessary to add previous shift
            for i in range(0, 3):
                G[3 + i] = [G[3 + i][j] - G[i][j] for j in range(0, len(G[3 + i]))]

        if relative:
            Ghx = list(np.array(G[3]) + np.array(G[0]))
            Ghy = list(np.array(G[4]) + np.array(G[1]))
            Ghz = list(np.array(G[5]) + np.array(G[2]))
            Gs = G[0] + G[1] + G[2] + Ghx + Ghy + Ghz

        Gs.append(0)  # if you need to see the origin of the coordinate system

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

    plt.quiver(G[0], G[1], G[2], G[3], G[4], G[5], arrow_length_ratio=0.1, colors='k')
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
