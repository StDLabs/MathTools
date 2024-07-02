from MathTools.ArrayTransform.AnalytGeom.plane_type import plane_type
import matplotlib.pyplot as plt


def plot_scalar_field_contour_map(M1, M2, F, LN, Title, Pl, P, Save):

    Axis = ('XYZ')
    plane_info = plane_type(Pl)
    s = plane_info[1][0]
    i1 = plane_info[3][0]
    i2 = plane_info[3][1]
    U = -Pl[3] / Pl[s]

    plt.figure(1, figsize=(6, 4))
    CS = plt.contourf(M1, M2, F, LN, cmap=plt.cm.gray)
    CB = plt.colorbar(CS, shrink=0.8, label=Title)
    CB.formatter.set_powerlimits((0, 0))
    CB.update_ticks()
    plt.xlabel('Axis ' + str(Axis[i1]) + ': [' + str(-P[i1]) + ', ' + str(P[i1]) + ' ]')
    plt.ylabel('Axis ' + str(Axis[i2]) + ': [' + str(-P[i2]) + ', ' + str(P[i2]) + ' ]')
    plt.title('Field section ' + Axis[s] + ' = ' + str(U))
    # plt.axes().set_aspect('equal')
    plt.grid(True)
    if s == 2:
        plt.gca().invert_yaxis()
    if Save:
        vv = 1
    else:
        plt.show()

    return
