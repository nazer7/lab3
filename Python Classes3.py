class Shape:
    def __init__ (self):
        self.area = 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rect = Rectangle(4, 6)
print("Rectangle Area:", rect.area())  