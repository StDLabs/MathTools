from MathTools.PointGenerators.SpatialFields.field_3d import field_3d
from MathTools.PointGenerators.PeriodStruct.periodic_structure_cartesian_points_3d import periodic_structure_cartesian_points_3d
import numpy as np
from mayavi.mlab import *
from mayavi import mlab


def plot_scalar_filed_contour_3d(P, MQ, LN, title_main, title_bar):
    """
    Description
        The plot_scalar_filed_contour_3d function generates a 3D contour plot of a scalar field using the Mayavi
        visualization library. It visualizes isosurfaces based on the provided scalar field data, displays a color bar,
        and includes axes and a title for reference

    :param P: P = [Px, Py, Pz] - defines the area bounds {{-Px,Px},{-Py,Py},{-Pz,Pz}} for calculations
    :param MQ: 3D array of scalar field data to be visualized
    :param LN: Number of contour levels to be drawn
    :param title_bar: Title for the color bar
    :return:
    """

    MQ = np.array(MQ)
    a = [0, 1, 0, P[1] / P[0], 0, P[2] / P[0]]
    mlab.figure(figure=1, size=(550, 325))
    contour3d(MQ, contours=LN, opacity=0.5, extent=a)
    mlab.colorbar(title=title_bar, orientation='vertical')
    mlab.axes(ranges=(-P[0], P[0], -P[1], P[1], -P[2], P[2]))
    mlab.title(title_main, size=0.3, height=0.95)
    mlab.outline(line_width=0.1, extent=a)
    mlab.draw()
    mlab.show()

    return


def plot_scalar_filed_contour_3d_example():

    H = [2, 2, 2]
    D = [0, 0, 0, 0, 0, 0]
    T = [5, 5, 5]
    Sh = [0, 0, 0]

    # G = [[0, 0, 0]]
    # Q = [1]

    G = periodic_structure_cartesian_points_3d(H, D, T, True, Sh)
    Q = [1 for i in range(0, len(G))]

    P = [10, 10, 10]
    N3d = [30, 30, 30]
    A = [1, 1, 0.5, 0]
    function = 'hyperbola'
    option = 'scalar'
    M, MQ = field_3d(P, N3d, G, Q, A, function, option)
    LN = 20
    title_main = 'title_main'
    title_bar = 'title_bar'
    plot_scalar_filed_contour_3d(P, MQ, LN, title_main, title_bar)

    return
