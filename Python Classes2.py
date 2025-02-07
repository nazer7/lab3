class Shape:
    def area(self):
        self.area = 0 
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
sq = Square(6)
print("Square Area:", sq.area()) 