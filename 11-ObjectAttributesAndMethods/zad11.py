import math

class SurfaceAreaCalculator:
    @staticmethod
    def triangle(base, height):
        return 0.5 * base * height
    
    @staticmethod
    def rectangle(length, width):
        return length * width
    
    @staticmethod
    def circle(radius):
        return math.pi * radius ** 2

print(SurfaceAreaCalculator.circle(3))

print(SurfaceAreaCalculator.rectangle(4, 7))

print(SurfaceAreaCalculator.triangle(6, 2))
