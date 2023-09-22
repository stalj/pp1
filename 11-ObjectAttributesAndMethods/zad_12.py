class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

point_1=Point(3,7)
point_2=Point(7,3)
print(point_1==point_2)