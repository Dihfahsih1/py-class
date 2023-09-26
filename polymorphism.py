# class Human():
#     def __init__(self,name,house,age):
#         self.name=name
#         self.house=house
#         self.age=age
#     def years():
#         print("I am {self.age} years old")
    
# man=Human("ham",15,27)



class Store():
    def __init__(self,job,price):
        self.job=job
        self.price=price
    def setjob(self,newjobb):
        self.newjob=newjobb
    def getjob(self):
        print("Its new job is {self.newjob}")
        
tractor=Store("dig",3900)
Store.setjob("prun")
tractor.setjob()


