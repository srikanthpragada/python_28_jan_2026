import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getradius(self):
        return self.radius

    def getarea(self):
        return math.pi * self.radius * self.radius

    def getCircumference(self):
        return  2 * math.pi * self.radius

c = Circle(10)
print(c.getarea())
