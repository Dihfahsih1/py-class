class Doctor():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def sleep(self):
        print(f"my name is doctor {self.name} and i usually sleep late")
        
    def operations(self):
        print(f"i have been doing operations till these {self.age} years")

Doctor1=Doctor('remi',24)
Doctor1.sleep()
Doctor1.operations()