# hiding internal fuctionality and showing only essential data

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# The following line would cause an error because you can't instantiate an abstract class
# shape = Shape()

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())