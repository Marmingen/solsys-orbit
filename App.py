#################################################################################
## IMPORTS

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import math
import numpy

from physclasses import *

#################################################################################

class App():
    
    def __init__(self):
        self.fig = plt.figure()
        self.ax = p3.Axes3D(self.fig)
        
        self.ax.set_xlabel('X')
        
        self.ax.set_ylabel('Y')
        
        self.ax.set_zlabel('Z')
        self.ax.set_zlim3d([-10, 10])
        
        self.system = System()
        self.points = []


    def draw_body(self):
        for body in self.system.bodies.values():
            body.calc_pos(0)
            self.points.append(self.ax.scatter(body.pos.x, body.pos.y, body.pos.z, color=body.color,\
                            marker='o', edgecolor="black", linewidth=1))
            
            
    def draw_ellipse(self):
        for body in self.system.bodies.values():
            body.calc_ellipse()
            self.ax.plot3D(body.ellipse[0], body.ellipse[1], body.ellipse[2],\
                alpha=0.25, color="black")
            
            
    def update(self):
        self.system.t += 1
        for point in self.points:
            #planet.calc_pos(times[frame])
            point._offsets3d = (0,0,0)

    # def frame(self, f, artists):
    #     self.system.t += 1
    #     for body in self.system.bodies.values():
        
    #         body.calc_pos(self.system.t)
    #         artists[0]._offsets3d = (body.pos.x, body.pos.y, body.pos.z)
            
    #     return artists[0]
            
    # def animate(self):        
        
    #     ani = animation.FuncAnimation(self.fig, 19, self.frame, fargs=(self.points),
    #                             interval=40, blit=True)
        
    #     return ani
        
      
    
    def show(self):
        plt.show()
        
    def close(self):
        plt.close()