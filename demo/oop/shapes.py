from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getpoint(self):
        return (self.x, self.y)

    @abstractmethod
    def getarea(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def getradius(self):
        return self.radius

    def getarea(self):
        return math.pi * self.radius ** 2


c = Circle(10, 10, 15)
print(c.getpoint())
print(c.getradius())
print(c.getarea())
