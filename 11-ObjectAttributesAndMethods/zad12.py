import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'P({self.x},{self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
def distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

p1 = Point(1, 2)
p2 = Point(1, 4)

if p1 == p2:
    print('The distance between the points is 0')
else:
    dist = distance(p1, p2)
    print(f'The distance between the points is {dist}')
