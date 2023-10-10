# TASK3

class Shape:
    def __init__(self, color):
        self.color = color

    def Area(self):
        return area 

    def DisplayColor(self):
        print (f"The shape is {self.color}")

class Circle(Shape):
    def area(self):
        area = (22/7) * (r*r)
        r = int(input("Enter radius value: "))
        print(area)

class Rectangle(Shape):
    def area(self):
        area = L * W
        L = int(input("Enter length: "))
        W = int(input("Enter width: "))
        print(area) 


s = Shape("red")
s.Shape()
