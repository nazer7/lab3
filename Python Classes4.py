import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f'x={self.x}  y={self.y}')
    def move(self, x2, y2):
        self.x = x2
        self.y = y2
    def dist(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
p1 = Point(3, 4)
p2 = Point(6, 8)
p1.show()
p2.show()
print("Distance:", p1.dist(p2))  