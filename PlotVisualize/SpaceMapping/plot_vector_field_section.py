from MathTools.PointGenerators.PeriodStruct.periodic_structure_cartesian_points_3d import periodic_structure_cartesian_points_3d
from MathTools.PointGenerators.SpatialFields.field_section import field_section
from MathTools.ArrayTransform.AnalytGeom.plane_type import plane_type
from mayavi import mlab
import numpy as np


def plot_vector_field_section(P, Pl, MQ, title_main, title_bar):

    Axis = ('XYZ')
    plane_info = plane_type(Pl)
    s = plane_info[1][0]
    i1 = plane_info[3][0]
    i2 = plane_info[3][1]
    U = -Pl[3] / Pl[s]

    a = [0, P[i1] / P[i2], 0, 1, 0, 0.03]
    mlab.quiver3d(MQ[i1], MQ[i2], MQ[s], extent=a)
    mlab.colorbar(title=title_bar, orientation='vertical')
    mlab.axes(ranges=(-P[i1], P[i1], -P[i2], P[i2], U, U), xlabel=str(Axis[i1]), ylabel=str(Axis[i2]), zlabel='')
    mlab.title(title_main, size=0.3, height=0.95)
    mlab.outline(line_width=0.1, extent=a)
    mlab.draw()
    mlab.show()

    return


def plot_vector_field_section_example():

    Pl = [0, 0, 1, -1]
    P = [10, 10, 10]
    Npl = [100, 100]

    H = [3, 3, 1]
    D = [0, 0, 0, 0, 0, 0]
    T = [5, 5, 5]
    Sh = [0, 0, 0]

    G = periodic_structure_cartesian_points_3d(H, D, T, True, Sh)
    Q = [1 for i in range(0, len(G))]

    # G = [[2.5, 2.5, 0], [-2.5, -2.5, 0]]
    # Q = [1, 1]

    A = [1, 2, 0.5, 0]
    function = 'hyperbola'
    option = 'vector'

    M1, M2, F = field_section(Pl, P, Npl, G, Q, A, function, option)

    MQ = np.transpose(np.array([F]), (3, 2, 1, 0)).tolist()

    title_main = 'title_main'
    title_bar = 'title_bar'
    plot_vector_field_section(P, Pl, MQ, title_main, title_bar)

    return
