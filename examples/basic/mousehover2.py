"""Compute 3D world coordinates from 2D screen pixel coordinates
(hover mouse to place the points)"""
from vedo import *

settings.defaultFont = "Ubuntu"
settings.useDepthPeeling = True


def func(evt):                 # this is the callback function
    i = evt.at                 # the renderer nr. which is being hit
    pt2d = evt.picked2d        # 2D screen coordinate
    # passing a list of meshes will force the points to be placed on any of them
    pt3d = plt.computeWorldPosition(pt2d, at=i, objs=[objs[i]])
    if mag(pt3d) < 0.01:
        return
    newpt = Point(pt3d).color(i)
    txt.text(f'2D coords: {pt2d}\n3D coords: {pt3d}\nNpt = {len(plt.actors)}')
    txt.color(i)               # update text and color on the fly
    plt.add(newpt, at=i)       # add new point and render


# create an empty text (to be updated in the callback)
txt = Text2D("", s=1.4, font='Brachium', c='white', bg='green8')

# create two polygonal meshes
mesh1 = TessellatedBox()
mesh2 = ParametricShape('ConicSpiral')
mesh2.c('indigo1').bc('tomato').lc('grey9').lw(0.1)
objs = [mesh1, mesh2]

plt = Plotter(N=2, bg='blackboard', axes=1, sharecam=False)
plt.addCallback('mouse move', func)

plt.show(mesh1, __doc__, at=0, viewup='z')
plt.show(mesh2, txt,     at=1, zoom=1.4)
plt.interactive().close()

