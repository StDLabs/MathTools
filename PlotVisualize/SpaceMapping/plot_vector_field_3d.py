from mayavi.mlab import *
from mayavi import mlab


def plot_vector_field_3d(P, MQ, Title, title_main, title_bar):

    a = [0, 1, 0, P[1] / P[0], 0, P[2] / P[0]]
    mlab.figure(figure=1, size=(550, 325))
    mlab.quiver3d(MQ[0], MQ[1], MQ[2], extent=a)
    mlab.colorbar(title=title_bar, orientation='vertical')
    mlab.axes(ranges=(-P[0], P[0], -P[1], P[1], -P[2], P[2]))
    mlab.title(title_main, size=0.3, height=0.95)
    mlab.outline(line_width=0.1, extent=a)
    mlab.draw()

    return
