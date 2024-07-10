from MathTools.PointGenerators.PeriodStruct.periodic_structure_cartesian_points_3d import periodic_structure_cartesian_points_3d
from MathTools.PointGenerators.SpatialFields.field_3d import field_3d
from mayavi.mlab import *
from mayavi import mlab
import numpy as np


def plot_vector_field_3d(P, MQ, title_main, title_bar):

    a = [0, 1, 0, P[1] / P[0], 0, P[2] / P[0]]
    mlab.figure(figure=1, size=(550, 325))
    mlab.quiver3d(MQ[0], MQ[1], MQ[2], extent=a)
    mlab.colorbar(title=title_bar, orientation='vertical')
    mlab.axes(ranges=(-P[0], P[0], -P[1], P[1], -P[2], P[2]))
    mlab.title(title_main, size=0.3, height=0.95)
    mlab.outline(line_width=0.1, extent=a)
    mlab.draw()
    mlab.show()

    return


def plot_vector_field_3d_example():

    H = [1, 1, 1]
    D = [0, 0, 0, 0, 0, 0]
    T = [5, 5, 5]
    Sh = [0, 0, 0]

    # G = [[0, 0, 0]]
    # Q = [1]

    G = periodic_structure_cartesian_points_3d(H, D, T, True, Sh)
    Q = [1 for i in range(0, len(G))]

    P = [10, 10, 10]
    N3d = [20, 20, 20]
    A = [1, 1, 0.5, 0]
    function = 'hyperbola'
    option = 'vector'
    M, MQ = field_3d(P, N3d, G, Q, A, function, option)
    title_main = 'title_main'
    title_bar = 'title_bar'

    MQ = np.transpose(np.array(MQ), (3, 0, 1, 2)).tolist()

    plot_vector_field_3d(P, MQ, title_main, title_bar)

    return
