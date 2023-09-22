class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def bark(self):
        return "Woof!"
        
# object
my_dog = Dog(name=input("Enter the Dog Name "), age=int(input("Enter the Dog age: ")))

print(my_dog.name)
print(my_dog.age)

print(my_dog.bark())