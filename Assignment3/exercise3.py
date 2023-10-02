"""class student which allows us to grade them \\\
    according to their age as seen[mature/minor]"""
class Student():
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def calculate_grades(self):
        if self.age <18:
            print("Your grade is minor")
        else:
            print("Your grade is mature")
    def __repr__(self):
        print(f"stdent('{self.name}','{self.age}','{self.grade}')")
            
stdent1=Student('marvin',17,"third")
stdent1.calculate_grades()
student2=Student('simon',20,'first')
student2.calculate_grades()
stdent1.__repr__()
student2.__repr__()


"""class methods and inheritance"""
class Vehicle():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class Car(Vehicle):
    def __init__(self,make,model,year,fueltype):
        super().__init__(make,model,year)
        self.fuel=fueltype
        print(f"my car uses {self.fuel}")
car1=Car('yamama','Gm20',1999,'petrol')
                         
class Bike(Vehicle):
    def __init__(self,make,model,year,wheelsize):
        super().__init__(make,model,year)
        self.wheel=wheelsize
        print(f"my wheel size is {wheelsize}")

"""create a class shape with those attributes\\(class methods and inheritance)
      and two other sub classes and override the method area"""
class Shape():
    def __init__(self,colour,length,width):
        self.colour=colour
        self.length=length
        self.width=width
    def area(self):
        print(self.width * self.length)
    def display_colour(self):
         print(self.colour)
box=Shape("red",19,18)
box.area()
box.display_colour()

class Circle(Shape):
    def __init__(self,colour,length,width,radius,diameter):
        super().__init__(colour,length,width)
        self.radius=radius
        self.diameter=diameter
    def area(self):
        print(self.radius * self.diameter)
semicircle=Circle('yellow',2,3,2,4)
semicircle.area()
semicircle.display_colour()

class Rectangle(Shape):
    def __init__(self, colour, length, width,height):
        super().__init__(colour, length, width)
        self.height=height
    def area(self):
        print(f"my area is {self.height * self.width}")
rec=Rectangle('blue',2,3,4)
rec.area()
rec.display_colour()
        
        

        


        