import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x},{self.y})"

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def get_length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)
    
    def normalize(self):
        length = self.get_length()
        if length == 0:
            return Vector(0, 0) 
        return Vector(self.x / length, self.y / length)

v1 = Vector(3, 4)
v2 = Vector(1, 1)
k = 5

print("add", (v1 + v2))
print("sub", (v1 - v2))
print("str", v1)
print("dot", (v1.dot(v2)))
print("length", v1.get_length())
print("mul", v1 * k)
print("normalize", v1.normalize())
