import math

class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example usage
shape = Shape()
square = Square(5)
rectangle = Rectangle(5, 10)
point1 = Point(1, 2)
point2 = Point(4, 6)

print("Shape area:", shape.area())  # Output: Shape area: 0
print("Square area:", square.area())  # Output: Square area: 25
print("Rectangle area:", rectangle.area())  # Output: Rectangle area: 50

point1.show()  # Output: Point(1, 2)
point1.move(3, 5)
point1.show()  # Output: Point(3, 5)
print("Distance:", point1.dist(point2))  # Output: Distance: 1.4142135623730951...
