class Man():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def num(self):
        print("you all stupid")
class Shap(Man):
    def __init__(self, name, age,school,status):
        super().__init__(name, age)
        self.school=school
        self.status=status
    def num(self):
        print("Y'all make sense")
pretty=Shap('macos',12,'shutter','single')
pretty.num()
