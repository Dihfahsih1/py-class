class Human:
    def __init__(self, name,age,gender):
        self.name=name
        self.age=age
        self.gender = gender
        
    def eat(self):
        print(f"am a human called{self.name} and i can eat! ")
        
    def walk(self):
        print(f"am a human aged{self.age} and i can walk! ")
        
human1 = Human("John", 32, "Male")
human1.eat()
human1.walk()