class Animal:
    def __init__(self, name, type):
        self.name=name
        self.type=type
        
    def speak(self):
        """It is empty because each animal speaks differently!"""
        pass
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} and of type {self.type}, says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} and of type {self.type}, says Meow!"
    
dog = Dog("German Shepherd", "Type-1")
cat = Cat("Cute-C", "Type-3")

print(dog.speak())
print(cat.speak())
    