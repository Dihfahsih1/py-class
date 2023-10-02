class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def bark(self):
        return "Woof!"
        
my_dog = Dog(b=input("Enter the Dog Name: "), a=int(input("Enter the Dog age: ")))

print(my_dog.name)
print(my_dog.age)

print(my_dog.bark())