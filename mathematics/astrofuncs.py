#################################################################################
## IMPORTS

import math
from .Matrix import Matrix
from constants import *
from .NR import new_rap
from mathematics import Vector

#################################################################################
## FUNCTIONS

def calc_period(a):
    return 2*math.pi*math.sqrt(a**3)/k

def mean_motion(period):
    return 2*math.pi/period

def mean_anamoly(n, t, T):
    return n*(t-T)

def calc_orb_pos(elements, E):
    # x = a*(cos(E)-e)
    x = elements[0]*(math.cos(E)-elements[1])
    
    # y = a*sqrt(1-e^2)sin(E)
    y = elements[0]*math.sqrt(1-elements[1]**2)*math.sin(E)
    
    return Vector(x,y,0)

def R_orb2ec(elements):
    i = elements[2]
    w = elements[3]
    W = elements[4]
    cos = math.cos
    sin = math.sin
    R11 = cos(W)*cos(w)-sin(W)*cos(i)*sin(w)
    R12 = -cos(W)*sin(w)-sin(W)*cos(i)*cos(w)
    R13 = sin(W)*sin(i)
    R21 = sin(W)*cos(w)+cos(W)*cos(i)*sin(w)
    R22 = -sin(W)*sin(w)+cos(W)*cos(i)*cos(w)
    R23 = -cos(W)*sin(i)
    R31 = sin(i)*sin(w)
    R32 = sin(i)*cos(w)
    R33 = cos(i)
    R = Matrix("R_orb2ec", R11, R12, R13, R21, R22, R23,\
        R31, R32, R33)
    return R