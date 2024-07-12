import datetime
from MathTools.log_files import check_log_folder
from MathTools.ArrayTransform.Restructuring.transpose_vector_field import transpose_vector_field
from MathTools.ArrayTransform.AnalytGeom.plane_type import plane_type
from MathTools.PointGenerators.PeriodStruct.periodic_structure_cartesian_points_3d import periodic_structure_cartesian_points_3d
import matplotlib.pyplot as plt
import numpy as np


def plot_dots_planes_3d(G: list, PL: list, P, input_type, planes_key, key_save, key_show):
    """
    Description
        This function creates a 3D plot that visualizes a set of points (dots) and planes in a 3D space

        input_type = 0 means G = [R0, R1, ...] - set of vectors Ri = [Rix, Riy, Riz].

        input_type = 1 means G = [Gx, Gy, Gz], Gx = [R1x, R2x, ... ], Gy = [R1y, R2y, ...], Gz = [R1y, R2y, ...].

    :param G: set of 3d vectors
    :param PL: PL = [Pl1, Pl2, ..., Pli], Pli = [Ai, Bi, Ci, Di] - set of planes (any)
    :param P: P = [Px, Py, Pz] - defines the area bounds {{-Px,Px},{-Py,Py},{-Pz,Pz}} for calculations
    :param input_type: input_type = 0, 1 (see description)
    :param planes_key: planes_key = True means Pl contains at least one plane necessary for drawing
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

    if planes_key:
        for i in range(0, len(PL)):
            plane_info = plane_type(PL[i])
            if plane_info[2] == 2:
                s = plane_info[1][0]
                i1 = plane_info[3][0]
                i2 = plane_info[3][1]
                U = -PL[i][3] / PL[i][s]
                K = np.arange(-P[i1], P[i1], P[i1] / 10)
                F = [0, 0, 0]
                F[i1], F[i2] = np.meshgrid(K, K)
                F[s] = (F[i1]**0 - F[i1]**0) + (F[i2]**0 - F[i2]**0) + U
                ax.plot_surface(F[0], F[1], F[2], alpha=0.5)
            else:
                X = np.arange(-5, 5, 0.25)
                Y = np.arange(-5, 5, 0.25)
                X, Y = np.meshgrid(X, Y)
                Z = -(PL[i][3] + PL[i][0] * X + PL[i][1] * Y) / PL[i][2]
                ax.plot_surface(X, Y, Z, alpha=0.5)

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


def plot_dots_planes_3d_example():

    H = [3, 3, 1]
    D = [0, 0, 0, 0, 0, 0]
    T = [5, 5, 5]
    Sh = [0, 0, 0]

    PL = [[1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1], [1, 1, 1, 0]]
    P = [10, 10, 10]

    G = periodic_structure_cartesian_points_3d(H, D, T, True, Sh)

    plot_dots_planes_3d(G, PL, P, input_type=0, planes_key=True, key_save=False, key_show=True)

    return
