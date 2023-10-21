import random
import numpy as np

from odio_urdf import *
from terrain_generator.link_generator import *

filename = "bumpy_terrain.urdf"
assert(filename[-5:] == ".urdf")

# table variables
[l,w,h] = 2, 1, 1
top_t = 0.1
[leg_l, leg_h] = [0.2*l, h-0.5*top_t]

def generateRandomTerrain(num=[], size=[5,5]):
    blocks = []
    blockSize = [size[0]/num[0],size[1]/num[1],random.gauss(0,1)]
    for i in range(num[0]):
        for j in range(num[1]):
            o = [i*blockSize(0),j*blockSize(1),0] - 0.5*[blockSize(0),blockSize(1),0] # TODO
            blocks[i,j] = rectangleLink(name=str(i)+str(j), dim=blockSize, o=o)
    return blocks

world = Link("world")
# ground = Link("ground", 
#               Inertial(Origin(xyz=[0,0,0]), Mass(value=0), Inertia(ixx=0,ixy=0,ixz=0,iyy=0,iyz=0,izz=0)),
#               Visual(Geometry(Mesh("plane.obj"))), 
#               Collision(Origin(xyz=[0,0,-0.1]), Geometry(Box([30,30,0.2]))), 
#               Contact(Lateral_Friction(1))
#             )
blocks = generateRandomTerrain(num=[1,1])
flattened_blocks = np.array(blocks).flatten()
joints = [Joint(str(k), Origin(xyz=[0,0,0]), Parent("world"), Child(flattened_blocks(k)), type="fixed") for k in range(len(flattened_blocks))]

terrain = Robot(
        "bumpy_terrain",
        world,
        *blocks,
        *joints,
    )

f = open(filename, mode='w')
f.write(repr(terrain))