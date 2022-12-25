#################################################################################
## IMPORTS

import numpy
from mathematics.Vector import Vector
from constants import J2000
from mathematics.astrofuncs import *
from mathematics.NR import new_rap
from math import radians

#################################################################################
## CELESTIAL BODY CLASS

class CelestialBody():
    
    def __init__(self, name="undefined", mass="0", orbital_elements=[0,0,0,0,0],\
        pos=Vector(0,0,0), color="black", T=J2000):
        
        self.name = name
        self.mass = mass
        
        # [a, e, i, w, W]
        self.orbital_elements = orbital_elements
        for i in range(2,5):
            self.orbital_elements[i] = radians(self.orbital_elements[i])
        
        self.pos = pos
        
        self.color = color
        
        self.P = calc_period(self.orbital_elements[0])
        self.n = mean_motion(self.P)
        
        if T == J2000:
            self.T = T
        else:
            self.T = nrml_to_JDT(T)
            
        self.R = R_orb2ec(self.orbital_elements)
        
        self.ellipse = [[],[],[]]
        
        self.lposx = []
        self.lposy = []
        self.lposz = []
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
    
    # updates the position according to the time
    def update_position(self, t):
        pass
    
    def calc_pos(self, t):
        
        # M
        M = mean_anamoly(self.n, t, self.T)

        # E, using Newton-Raphson
        E = new_rap(10, M, self.orbital_elements[1])
        
        self.pos = calc_orb_pos(self.orbital_elements, E)
        
        self.pos = self.R*self.pos
        
        self.lposx.append(self.pos.x)
        self.lposy.append(self.pos.y)
        self.lposz.append(self.pos.z)        

    
    def calc_ellipse(self):
        for i in numpy.linspace(0,2*math.pi,400):
            pos = self.R*calc_orb_pos(self.orbital_elements, i)
            self.ellipse[0].append(pos.x)
            self.ellipse[1].append(pos.y)
            self.ellipse[2].append(pos.z)
    
#################################################################################
## __main__

if __name__ == "__main__":
    CelestialBody()