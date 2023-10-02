from exercise1 import Student
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, owner):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.owned=owner


class Bike(Vehicle):
    def __init__(self, make, model, year, wheel_size):
        super().__init__(make, model, year)
        self.wheel_size = wheel_size


# Create Car and Bike objects and set their attributes
car = Car("Toyota", "Camry", 2022, "Gasoline", "Not Me")
bike = Bike("Trek", "Mountain Bike", 2021, 26)

# Print vehicle details
print("Car Details:")
print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}, Fuel Type: {car.fuel_type} and it is owned by: {car.owned}")

print("\nBike Details:")
print(f"Make: {bike.make}, Model: {bike.model}, Year: {bike.year}, Wheel Size: {bike.wheel_size}")
