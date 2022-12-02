#################################################################################
## IMPORTS

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np

from physclasses import *
from configsolsys import test_object

#################################################################################

class App():
    
    def __init__(self, time, speed):
        self.fig = plt.figure()
        self.ax = p3.Axes3D(self.fig)
        
        self.ax.set_xlabel('X')
        
        self.ax.set_ylabel('Y')
        
        self.ax.set_zlabel('Z')
        self.ax.set_zlim3d([-10, 10])
        
        self.time = time
        self.speed = speed
        
        self.system = System()
        self.artists = []


    def draw_body(self):
        for body in self.system.bodies.values():
            body.calc_pos(0)
            self.artists.append(self.ax.scatter(body.pos.x, body.pos.y, body.pos.z, color=body.color,\
                            marker='o', edgecolor="black", linewidth=1))
            
    def init_ellipse(self):
        for body in self.system.bodies.values():
            body.calc_ellipse()
            self.ax.plot3D(body.ellipse[0], body.ellipse[1], body.ellipse[2],\
                alpha=0.25, color="black")
            
    def initial_calculation(self):
        self.init_ellipse()
        self.draw_body()
        for t in range(1,self.time):
            for body in self.system.bodies.values():
                body.calc_pos(t)
                
        self.data = self.system.bodies.values()
            

    def frame(self, numb, data, artists):
        data = list(data)
        
        assert isinstance(data[0].lposx[0],float)
        
        for body, artist in zip(data, artists):
        
            body.calc_pos(self.system.t)
            
            artist._offsets3d = (np.array([body.lposx[numb]]), np.array([body.lposy[numb]]),\
                np.array([body.lposz[numb]]))

        return artists
            
            
    def animate(self):        
        
        
        ani = animation.FuncAnimation(self.fig, self.frame, self.time, fargs=(self.data, self.artists),
                                interval=40, blit=False)
        
        self.show()
        
        return ani
        
      
    
    def show(self):
        plt.show()
        
    def close(self):
        plt.close()
        
        
if __name__ == "__main__":
    app = App(200)
    
    test_object(app)
    
    app.initial_calculation()
    
    anim = app.animate()