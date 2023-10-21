from odio_urdf import *
from terrain_generator.link_generator import *

filename = "wall.urdf"
assert(filename[-5:] == ".urdf")

# table variables
[l,w,h] = 2, 0.5, 2

wall = rectangleLink("wall", dim=[l,w,h], o=[0,0,h/2])

terrain = Robot(
        "wall",
        wall,
)

f = open(filename, mode='w')
f.write(repr(terrain))