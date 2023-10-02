##learning python programming functions 
def calculate():
    number=int(input("whats yr fav number: "))
    cal=number**4
    print(cal)
calculate()


num=lambda x:x**2
print(num(2))
class Man():
    def __init__(self,name,status,religion):
        self.name=name
        self.status=status
        self.religion=religion
    def cry(self):
        print("a man crys less")
class Boy(Man):
    def __init__(self,name,status,religion,age):
        super().__init__(name,status,religion)
        self.age=age
    def cry(self):
        print("a boy over cries")
        print(f"my name is {self.name} and am {self.age} years old")

boy=Boy('mad','single','cath',23)
boy.cry()


        

    