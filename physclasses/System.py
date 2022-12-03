#################################################################################
## IMPORTS

from physclasses import *
from mathematics import *

#################################################################################
## SYSTEM CLASS

class System():
    
    def __init__(self):
        
        self.bodies = {}
        self.mass = 0
        self.h = Vector(0,0,0)
    
    def update(self):
        self.total_mass = 0
        self.h = Vector(0,0,0)
        
        for object in self.bodies:
            self.total_mass+=object.mass
            self.h += object.h
    
    def add_body(self, body):
        self.bodies[body.name] = body