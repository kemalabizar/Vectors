class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        "Returns the value of self vector, represented as [x, y, z] components."
        return str(f'[{self.x}, {self.y}, {self.z}]')
    def typecheck(self):
        "Checks if self is vector or not. Usually only implemented in vector-vector operations."
        if type(self) is not Vec3:
            raise ValueError("ERROR: Operand is not a vector")
        else: pass
    def mag(self):
        "Returns the self vector's magnitude."
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __add__(self, b):
        "Returns self + b, both being Vec3()."
        b.typecheck()
        return Vec3(self.x+b.x, self.y+b.y, self.z+b.z)
    def __sub__(self, b):
        "Returns self - b, both being Vec3()."
        b.typecheck()
        return Vec3(self.x-b.x, self.y-b.y, self.z-b.z)
    def dot(self, b):
        "Returns dot product of self with b."
        b.typecheck()
        return (self.x*b.x + self.y*b.y + self.z*b.z)
    def cross(self, b):
        "Returns cross product of self with b."
        b.typecheck()
        return Vec3((self.y*b.z - self.z*b.y), (self.z*b.x - self.x*b.z), (self.x*b.y - self.y*b.x))
    def __mul__(self, b):
        "Returns scalar product of self with a scalar b."
        if type(b) is Vec3:
            raise ValueError("ERROR: Operand cannot be a vector, must be scalar")
        else:
            return Vec3(self.x*b, self.y*b, self.z*b)
    def __div__(self, b):
        "Returns scalar product of self with a scalar 1/b."
        if type(b) is Vec3:
            raise ValueError("ERROR: Operand cannot be a vector, must be scalar")
        else:
            return Vec3(self.x/b, self.y/b, self.z/b)