class Animal:
    def __init__(self, name, type_of_animal):
        self.name = name
        self.type_of_animal = type_of_animal
        
        
    def speak(self):
        pass
      
        
class Dog(Animal):
    def speak(self):
        print(f"My name is{self.name} and I am a {self.type_of_animal} that ")
        return "woof"

class Cat(Animal):
    def speak(self):
        print(f"My name is{self.name} and I am a {self.type_of_animal} that ")
        return "mweoo"
        
Dog = Dog("max", "Chiwawa")
Cat = Cat("kitty", "ginger cat")
print(Dog.speak())
print(Cat.speak())
