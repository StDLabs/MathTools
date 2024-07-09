from MathTools.PointGenerators.SpatialFields.scalar_field_3d import scalar_field_3d
from MathTools.PointGenerators.PeriodStruct.periodic_structure_cartesian_points_3d import periodic_structure_cartesian_points_3d
import numpy as np
from mayavi.mlab import *
from mayavi import mlab


def plot_scalar_filed_contour_3d(P, MQ, LN, Title):

    MQ = np.array(MQ)
    a = [0, 1, 0, P[1] / P[0], 0, P[2] / P[0]]
    mlab.figure(figure=1, size=(550, 325))
    contour3d(MQ, contours=LN, opacity=0.5, extent=a)
    mlab.colorbar(title=Title, orientation='vertical')
    mlab.axes(ranges=(-P[0], P[0], -P[1], P[1], -P[2], P[2]))
    mlab.title('Scalar field isosurfaces', size=0.3, height=0.95)
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
    M, MQ = scalar_field_3d(P, N3d, G, Q, A, function)
    LN = 20
    Title = 'Name'
    plot_scalar_filed_contour_3d(P, MQ, LN, Title)

    return
