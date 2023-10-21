from odio_urdf import *

def rectangleGeometry(dim):
    assert(len(dim) == 3)
    return Geometry(Box(dim))

def rectangleLink(name="", dim=[], o=[], *args):
    ''' create rectangular link with visual and collision '''
    assert(len(o) == 3)
    rec = rectangleGeometry(dim)
    ori = Origin(o)
    return Link(name, Visual(ori, rec), Collision(ori, rec), *args)

def saveToFile(filename, odio):
    f = open(filename, mode='w')
    f.write(repr(odio))