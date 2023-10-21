from terrain_generator.link_generator import *
import numpy as np

h = 0.1 # height
x_0 = 1
x_1 = 0.5*x_0 
y_0 = 0.5
y_1 = 0.5
h_1 = 2*h # obstacle height
h_w = 0.5 # wall height

x_w = 0.1
y_w = y_1
z_w = 0.1

platform_dim = [x_0,y_0,h]
mid_platform_dim = [x_1,y_1,h]
obs_dim = [x_0-x_1,y_1,h_1]
wall_dim = [x_w,y_w,z_w]
d = 0.1 # offset distance for wall

start_origin = np.array([0,0.5*y_0,0.5*h])
mid_origin = start_origin + np.array([0.5*(x_1-x_0),0.5*(y_0+y_1),0])
end_origin = start_origin + np.array([0,y_0+y_1,0])
obs_origin = mid_origin + np.array([0.5*(x_1+obs_dim[1]),0,0.5*h_1])
wall_origin = start_origin + np.array([0.5*(x_0+x_w+d),0.5*(y_0+y_1),0.5*z_w+h_w])

world = Link("world")
obstacle = rectangleLink("obstacle",dim=obs_dim,o=[0,0,0])
start = rectangleLink("start",dim=platform_dim,o=[0,0,0])
middle = rectangleLink("middle",dim=mid_platform_dim,o=[0,0,0])
end = rectangleLink("end",dim=platform_dim,o=[0,0,0])
side_wall = rectangleLink("wall",dim=wall_dim, o=[0,0,0])

terrain = Robot(
    world,
    obstacle,
    side_wall,
    start,
    middle,
    end,
    Joint("1",
          Origin(xyz=start_origin.tolist()),
          Parent("world"),
          Child("start"),
          type="fixed",
    ),
    Joint("2",
          Origin(xyz=mid_origin.tolist()),
          Parent("world"),
          Child("middle"),
          type="fixed",
    ),
    Joint("3",
          Origin(xyz=end_origin.tolist()),
          Parent("world"),
          Child("end"),
          type="fixed",
    ),
    Joint("obs",
          Origin(xyz=obs_origin.tolist()),
          Parent("world"),
          Child("obstacle"),
          type="fixed",
    ),
    Joint("wall",
          Origin(xyz=wall_origin.tolist()),
          Parent("world"),
          Child("wall"),
          type="fixed",
    ),
    Material(Color(rgba=[39,146,245,0.8])),
)

saveToFile("terrain1.urdf", terrain)