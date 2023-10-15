class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def description(self):
        print(f"Hey! My name is {self.name}, I am a {self.gender} and am {self.age} years old")

class boy(Human):
    def schoolName(self, schoolname):
        print(f"I study in {schoolname}")
b = boy('Edcorner', 32, 'male')
b.description()
b.schoolName("MIT")