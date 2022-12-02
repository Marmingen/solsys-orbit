import numpy as np
import sympy

""" 
Newton-Raphson method for numerically
solving the Kepler equation
"""
def new_rap(n, M, e):
    E = sympy.symbols('E')
    
    f = E-e*sympy.sin(E)-M
    
    # derivative, analytically done
    fprim = 1-e*sympy.cos(E)
    
    # good first-value is M
    # due to Taylor-expansion of sine
    En = M
    
    for _ in range(n):
        En = En - np.float(f.evalf(subs= {E:En})) / np.float(fprim.evalf(subs= {E:En}))
    
    return En    

if __name__ == "__main__":
    i = new_rap(2, 3, 2)