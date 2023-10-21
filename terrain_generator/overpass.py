from odio_urdf import *
from terrain_generator.link_generator import *

filename = "overpass.urdf"
assert(filename[-5:] == ".urdf")

# table variables
[l,w,h] = 2, 1, 1
top_t = 0.1
[leg_l, leg_h] = [0.2*l, h-0.5*top_t]

# world = Link("world")
# ground = Link("ground", 
#               Inertial(Origin(xyz=[0,0,0]), Mass(value=0), Inertia(ixx=0,ixy=0,ixz=0,iyy=0,iyz=0,izz=0)),
#               Visual(Geometry(Mesh("plane.obj"))), 
#               Collision(Origin(xyz=[0,0,-0.1]), Geometry(Box([30,30,0.2]))), 
#               Contact(Lateral_Friction(1))
#             )
top_surface = rectangleLink("top_surface", dim=[l,w,top_t], o=[0,0,h])
leg1 = rectangleLink("leg1", dim=[leg_l,w,leg_h], o=[0,0,0])
leg2 = rectangleLink("leg2", dim=[leg_l,w,leg_h], o=[0,0,0])

terrain = Robot(
        "overpass",
        top_surface,
        leg1,
        leg2,
        Joint("side1", 
                Origin(xyz=[0.5*(l-leg_l),0,0.5*leg_h], rpy=[0,0,0]), 
                Parent("top_surface"), 
                Child("leg1"), 
                type="fixed",
            ),
        Joint("side2",
                Origin(xyz=[-0.5*(l-leg_l),0,0.5*leg_h], rpy=[0,0,0]),
                Parent("top_surface"),
                Child("leg2"),
                type="fixed"
            )
    )

f = open(filename, mode='w')
f.write(repr(terrain))