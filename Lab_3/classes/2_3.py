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

shape = Shape()
print("Area of Shape:", shape.area())

length = int(input("Enter the length of the square: "))
square = Square(length)
print("Area of Square:", square.area())

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)
print("Area of Rectangle:", rectangle.area())
