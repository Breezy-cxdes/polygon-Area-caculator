import math

# Base class Polygon
class Polygon:
    def area(self):
        pass

# Triangle class inheriting Polygon
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Rectangle class inheriting Polygon
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Square class inheriting Polygon
class Square(Polygon):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# Circle class inheriting Polygon
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

# Main code to calculate areas
def main():
    # Create objects for each shape
    triangle = Triangle(base=10, height=5)
    rectangle = Rectangle(length=10, width=5)
    square = Square(side=4)
    circle = Circle(radius=3)
    
    # Print areas of the polygons
    print(f"Area of the triangle: {triangle.area()}")
    print(f"Area of the rectangle: {rectangle.area()}")
    print(f"Area of the square: {square.area()}")
    print(f"Area of the circle: {circle.area()}")

if __name__ == "__main__":
    main()
