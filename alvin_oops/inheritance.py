# TASK2

class Vehicle:
    def __init__(self, Make, Model, Year):
        self.Make = Make
        self.Model = Model
        self.Year = Year

class Car(Vehicle):
    def FuelType(self):
        return "Diesel"

class Bike(Vehicle):
    def WheelSize(self):
        return "32"

b = Car('Mercedes Benz', 'E-class', 2020)
m = Bike('Bugatti', 'Centurion', 2019)

print(b.FuelType())
print(m.WheelSize())


