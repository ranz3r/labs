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

# Example usage
shape = Shape()
square = Square(5)
rectangle = Rectangle(5, 10)

print("Shape area:", shape.area())  # Output: Shape area: 0
print("Square area:", square.area())  # Output: Square area: 25
print("Rectangle area:", rectangle.area())  # Output: Rectangle area: 50
