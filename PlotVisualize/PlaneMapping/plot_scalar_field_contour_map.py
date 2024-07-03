from MathTools.ArrayTransform.AnalytGeom.plane_type import plane_type
from MathTools.log_files import check_log_folder
import matplotlib.pyplot as plt
import datetime


def plot_scalar_field_contour_map(M1, M2, F, LN, Title, Pl, P, Save, layout):
    """
    Description
        This function generates and displays a contour map of a scalar field over a 2D grid section defined by a plane
        in 3D space. It can visualize the field with different color schemes and optionally save the plot.
        Supports different visualization styles ("DarkBlue" and "White"), with easy change of aspects and colors.
        Labels the axes based on the plane orientation and includes a detailed title. The function chooses the correct
        plane orientation and adjusts the plot labels accordingly.

    :param M1: The x-coordinates (or y, z depending on the plane orientation) of the 2D grid points
    :param M2: The y-coordinates (or x, z depending on the plane orientation) of the 2D grid points
    :param F: A 2D array representing the scalar field values at the grid points defined by M1 and M2.
    :param LN: The number of contour levels to draw
    :param Title: The title of the contour plot, often describing the field being visualized
    :param Pl: Pl = [A, B, C, D]. Parameters of the plane in the form Ax+By+Cz+D=0
    :param P: P = [Px, Py, Pz] - defines the area bounds {{-Px,Px},{-Py,Py},{-Pz,Pz}} for calculations
    :param Save: Flag to determine whether the plot should be saved to a file (True) or displayed (False).
    :param layout: Specifies the color scheme and style for the contour plot.
        Supported values are 'DarkBlue' and 'White' with labels.
    :return:
    """

    Axis = ('XYZ')
    plane_info = plane_type(Pl)
    s = plane_info[1][0]
    i1 = plane_info[3][0]
    i2 = plane_info[3][1]
    U = -Pl[3] / Pl[s]

    plt.figure(1, figsize=(6, 5))
    if layout == 'DarkBlue':
        CS = plt.contourf(M1, M2, F, LN, cmap=plt.cm.bone)  # YlGnBu
    if layout == 'White':
        CS = plt.contour(M1, M2, F, LN, alpha=1, cmap=plt.cm.viridis, linewidths=0.8)
        CL = plt.clabel(CS, CS.levels, inline=True, fontsize=7, rightside_up=True, inline_spacing=5)
        for label in CL:
            label.set_rotation(0)
    CB = plt.colorbar(CS, shrink=0.8, label=Title)
    CB.formatter.set_powerlimits((0, 0))
    CB.update_ticks()
    plt.xlabel('Axis ' + str(Axis[i1]) + ': [' + str(-P[i1]) + ', ' + str(P[i1]) + ' ]')
    plt.ylabel('Axis ' + str(Axis[i2]) + ': [' + str(-P[i2]) + ', ' + str(P[i2]) + ' ]')
    plt.title('Field section ' + Axis[s] + ' = ' + str(U))
    # plt.axes().set_aspect('equal')
    # plt.grid(True, color='0.8')
    if s == 2:
        plt.gca().invert_yaxis()
    if Save:
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        N, P = check_log_folder()
        plt.savefig(
            'Data/Chapter ' + str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '/' + str(N) + '.' + str(
                P + 1) + '.png')
    else:
        plt.show()

    return
