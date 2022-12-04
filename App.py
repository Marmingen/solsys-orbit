#################################################################################
## IMPORTS

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np

from physclasses import *
from configsolsys import test_object, comets
from constants import J2000
from mathematics.astrofuncs import nrml_to_JDT, JDT_to_nrml

#################################################################################
## APP CLASS

class App():
    
    def __init__(self, time=1, speed=10, interval=1, date=J2000):
        self.fig = plt.figure()
        self.ax = p3.Axes3D(self.fig)
        # plt.title("hey", loc="left")
        
        self.date_title = plt.suptitle("", y=0.98, x=0.15)
        
        self.ax.set_xlabel('X [au]')
        
        self.ax.set_ylabel('Y [au]')
        
        self.ax.set_zlabel('Z [au]')
        self.ax.set_zlim3d([-10, 10]) # for not exaggerating the inclination
        
        # self.fig.suptitle("hey")
        
        if date == J2000:
            self.date = date
        else:
            self.date = nrml_to_JDT(date)
            
        self.og_date = self.date
        
        self.set_time(time)
        self.set_speed(speed)
        self.set_interval(interval)
        
        self.system = System()
        self.artists = []
        # self.labels = []
        
        self.ax.scatter(0,0,0,color="yellow",marker='o', edgecolor="black", label="Sun")
        
        
        
    def set_time(self, t):
        self.time = t
    
    def set_speed(self, speed):
        self.speed = 1000/speed
    
    def set_interval(self, interval):
        self.interval = interval
        
    def set_date(self, date):
        self.date = nrml_to_JDT(date)
        self.og_date = self.date

    def update_date_title(self):
        self.date_title.set_text(f"date: {JDT_to_nrml(self.date)}")

    def draw_body(self):
        """creates a scatterplot for all bodies in self.bodies"""
        for body in self.system.bodies.values():
            body.calc_pos(self.date)
            # self.labels.append(self.ax.text(body.pos.x, body.pos.y, body.pos.z, body.name, size=8))
            self.artists.append(self.ax.scatter(body.pos.x, body.pos.y, body.pos.z, color=body.color,\
                            marker='o', edgecolor="black", linewidth=1, label=body.name))
            
            
    def init_ellipse(self):
        """the orbit will be constants due to perturbations being ignored
        thus the ellipse only has to be calculated once"""
        for body in self.system.bodies.values():
            body.calc_ellipse()
            self.ax.plot3D(body.ellipse[0], body.ellipse[1], body.ellipse[2],\
                alpha=0.25, color="black")
            
            
    def initial_calculation(self):
        """the first call after adding all celestial bodies"""
        self.init_ellipse()
        self.draw_body()
        for t in range(0,self.time, self.interval):
            for body in self.system.bodies.values():
                body.calc_pos(self.date + t)
                
        self.data = self.system.bodies.values()
        self.ax.legend(loc="lower right")
        

    def frame(self, numb, data, artists):
        """frame-method for the matplotlib animation"""
        data = list(data)
        
        self.date += self.interval
        
        if numb == 0:
            self.date = self.og_date
        
        self.update_date_title()
             
        for body, artist in zip(data, artists):
            artist._offsets3d = (np.array([body.lposx[numb]]), np.array([body.lposy[numb]]),\
                np.array([body.lposz[numb]]))

        return artists
            
            
    def animate(self):        
        """matplotlib animation with self.speed ms interval between frames"""
        ani = animation.FuncAnimation(self.fig, self.frame,\
            int(len(list(self.system.bodies.values())[0].lposx)),\
            fargs=(self.data, self.artists), interval=self.speed, blit=False)

        self.show()

        return ani
        
    
    def save(self, anim, path):
        writergif = animation.PillowWriter(fps=30)
        
        anim.save(path, writer=writergif)
    
    def show(self):
        plt.show()
        
        
    def close(self):
        plt.close()
        
#################################################################################
## RUN CODE
        
if __name__ == "__main__":
       
    app = App(300,60,10)
    
    app.set_date("1985-01-01-00")
    
    test_object(app)
    
    #comets(app)
    
    app.initial_calculation()
    
    anim = app.animate()
    
    # app.save(anim, "halley_passage.gif")