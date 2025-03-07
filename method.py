class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y  # For rectangles or squares
# parent class (Shape) constructor
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)  # Call the parent constructor

    def area(self):
        return 3.14 * self.radius ** 2  # Formula for the area of a circle

# Create an instance of Shape
Pi = Shape(3, 5)
print(Pi.area())  # Outputs: 15

# Create an instance of Circle
Ci = Circle(5)
print(Ci.area())  # Outputs: 78.5 (approx)
