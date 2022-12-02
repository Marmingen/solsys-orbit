from math import sqrt

class Vector():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
        # for use in matrix ops
        self.rowop = [x,y,z]
        
    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"
    
    def __repr__(self):
        return self.__str__()
    
    # norm of vector
    def norm(self):
        ab = abs(self)
        return Vector(self.x/ab, self.y/ab, self.z/ab)
    
    # rounds vector, returns list of coords
    def rnd(self):
        return [round(a,4) for a in self.rowop]
    
    # cross product
    def cross(self, other):
        x = self.y*other.z - self.z*other.y
        y = self.z*other.x - self.x*other.z
        z = self.x*other.y - self.y*other.x
        return Vector(x,y,z)
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x,y,z)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x,y,z)
    
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__rmul__(other)
        if not isinstance(other, Vector):
            return other.__rmul__(self)
        return self.x*other.x+self.y*other.y+self.z*other.z
    
    def __rmul__(self, other):
        return Vector(other*self.x, other*self.y, other*self.z)

        
if __name__ == "__main__":
    v = Vector(2,2)
    v2 = Vector(-2.22,-4.3333333333,2.32)
    print(abs(v2))