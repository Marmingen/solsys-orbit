from .Vector import Vector

class Matrix():
    def __init__(self, name="Matrix", r11=0, r12=0, r13=0, \
                r21=0, r22=0, r23=0,\
                r31=0, r32=0, r33=0):
        
        self.name = name
        
        self.elements = [[r11,r12,r13],\
                        [r21,r22,r23],\
                        [r31,r32,r33]]
        
    def __str__(self):
        return f"{self.elements[0]}\n{self.elements[1]}\n{self.elements[2]}"
    
    # shorthand name
    def __repr__(self):
        return self.name
    
    def __mul__(self,other):
        if isinstance(other,int):
            return self.__rmul__(other)
        elif isinstance(other, Vector):
            res = [0,0,0]
            for i, row in enumerate(self.elements):
                res[i] = sum([a*b for a, b in zip(other.rowop,row)])
            return Vector(res[0], res[1], res[2])
    
    def __rmul__(self,other):
        if isinstance(other, int):
            for row in self.elements:
                for i in range(len(row)):
                    row[i] *= other
            return self
        elif isinstance(other, Vector):
            res = [0,0,0]
            for i in range(3):
                for j in range(3):
                    res[i] += other.rowop[i]*self.elements[j][i]
            return Vector(res[0], res[1], res[2])

    """ 
    the determinant
    """
    def __abs__(self):
        frst = self.elements[0][0]*(self.elements[1][1]*self.elements[2][2]\
            -self.elements[1][2]*self.elements[2][1])
        scnd = self.elements[0][1]*(self.elements[1][0]*self.elements[2][2]\
            -self.elements[1][2]*self.elements[2][0])
        thrd = self.elements[2][2]*(self.elements[1][0]*self.elements[2][1]\
            -self.elements[1][1]*self.elements[2][0])
        
        return frst + scnd + thrd
    
if __name__ == "__main__":
    M = Matrix(r32=2, name="R")
    v = Vector(2,2,2)
    
    print(v*M)