class Shape:
    color = "red"

    def area(self):
        pass
    '''empty function'''

    def display_color(self):
        print(f"The color of the shape is {self.color}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


# Create Circle and Rectangle objects and set their attributes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and display areas of the shapes
print(f"Circle Area: {circle.area()}")
print(f"Rectangle Area: {rectangle.area()}")

# Display the color of the shapes
circle.display_color()
rectangle.display_color()
