from MathTools.PointGenerators.PeriodStruct.periodic_structure_cartesian_points_3d import periodic_structure_cartesian_points_3d
from MathTools.PointGenerators.SpatialFields.field_3d import field_3d
from mayavi import mlab
import numpy as np


def plot_field_lines_3D(P, MQ, seed_resolution, seed_visible, title_main, title_bar):

    mlab.flow(MQ[0], MQ[1], MQ[2],
              seed_resolution=seed_resolution,
              seed_visible=seed_visible,
              line_width=4,
              integration_direction='both')
    mlab.axes(ranges=(-P[0], P[0], -P[1], P[1], -P[2], P[2]))
    mlab.colorbar(title=title_bar, orientation='vertical')
    mlab.title(title_main, size=0.3, height=0.95)
    mlab.draw()
    mlab.show()

    return


def plot_field_lines_3D_example():
    
    H = [2, 1, 1]
    D = [0, 0, 0, 0, 0, 0]
    T = [5, 5, 5]
    Sh = [0, 0, 0]

    # G = [[0, 0, 0]]
    # Q = [1]

    G = periodic_structure_cartesian_points_3d(H, D, T, True, Sh)
    Q = [(-1)**i for i in range(0, len(G))]

    P = [10, 10, 10]
    N3d = [30, 30, 30]
    A = [1, 1, 0.5, 0]
    function = 'hyperbola'
    option = 'vector'
    M, MQ = field_3d(P, N3d, G, Q, A, function, option)
    title_main = 'title_main'
    title_bar = 'title_bar'
    seed_resolution = 15
    seed_visible = True

    MQ = np.transpose(np.array(MQ), (3, 0, 1, 2)).tolist()

    plot_field_lines_3D(P, MQ, seed_resolution, seed_visible, title_main, title_bar)

    return
