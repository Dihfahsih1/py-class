
class Human():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def description(self):
        print(f"my name is {self.name},am a {self.gender},and am {self.age} years old")
        

class Boy(Human):
    def SchoolName(self,schoolname):
        print(f"my school is {schoolname}")
boy1=Boy('dan',24,'male')
boy1.description()
boy1.SchoolName('Rise')


class Animal():
    def __init__(self,name,type):
        self.name=name
        self.type=type
        
    def speak(self):
            pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} and of type {self.type} says woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} and of type {self.type},says meew"
    
dog=Dog("German shepherd","Type-1")
cat=Cat('Cutee','Type-2')



