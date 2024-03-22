import datetime
from MathTools.log_files import check_log_folder
import numpy as np
import matplotlib.pyplot as plt


def plot_sets_of_functions_3d(W: dict, key_save: bool, key_show: bool):
    """
    Description
        W = {'W1': {'S': S1, 'ttl': ttl1, 'axisX': axisX1, 'axisY': axisY1, 'axisZ': axisZ1}, 'W2': { ... }, ... }
        - dict of sets.

        Si = {'F1': {'X': X1, 'Y': Y1, 'Z': Z1, 'T': T1, 'Label': Label1},
        'F2': { ... }, ... } - dict of functions for set i.

        Xi = [Xi1, Xi2, ..., XiJi], Yi = [Yi1, Yi2, ..., YiJi], Zi = [Zi1, Zi2, ..., ZiJi].

        Ti = 'Line' OR 'Dots' OR 'Dash' - style of line for each function.

        ttli = '...' - title for set i

        axisXi = '...', axisYi = '...', axisZi = '...' - names of axes for set i

        Labeli = '...' - names of each function


    :param W: set of sets of functions
    :param key_save: True/False - whether save or not
    :param key_show: True/False - whether show or not
    :return:
    """

    if key_save & key_show:
        print("plot_sets_of_functions_3d. Cannot show and save at the same time")
    if key_save:
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        N, P = check_log_folder()

    height_of_picture = 13
    kW = list(dict.keys(W))
    E = np.eye(3)  # matrix [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    C = ['b', 'g', 'r']  # colors for axes X, Y, Z

    for i in range(0, len(kW)):
        fig = plt.figure(i, figsize=(height_of_picture, 768 * height_of_picture / 1366))  # for 1366 x 768 screen
        ax = fig.add_subplot(111, projection='3d')

        # plot colored axes x, y, z
        for s in range(0, 3):
            plt.quiver(0, 0, 0, E[s][0], E[s][1], E[s][2], arrow_length_ratio=0.1, colors=C[s])

        plt.title(W[kW[i]]['ttl'])
        kS = list(dict.keys(W[kW[i]]['S']))
        for j in range(0, len(kS)):
            T = W[kW[i]]['S'][kS[j]]['T']
            X = W[kW[i]]['S'][kS[j]]['X']
            Y = W[kW[i]]['S'][kS[j]]['Y']
            Z = W[kW[i]]['S'][kS[j]]['Z']
            Label = W[kW[i]]['S'][kS[j]]['Label']
            if T == 'Line':
                plt.plot(X, Y, Z, color='k', linewidth=1, label=Label)  # plot(X, Y, Z) for lines
            if T == 'Dots':
                for s in range(0, len(W[kW[i]]['S'][kS[j]]['X'])):
                    plt.plot(X[s], Y[s], Z[s], 'ko', label=Label)  # plot(X, Y, Z) for dots
            if T == 'Dash':
                plt.plot(X, Y, Z, '--', color='k', linewidth=1, label=Label)  # plot(X, Y, Z) for dashed line
        ax.set_aspect('auto', adjustable='box')
        plt.grid()

        if key_show:
            plt.show()
        if key_save:
            plt.savefig(
                'Data/Chapter ' + str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '/' + str(N) + '.' + str(
                    P + 1 + i) + '.png')

    return
