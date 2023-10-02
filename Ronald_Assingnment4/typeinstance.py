##when we type, we want to show which class is our variable
nam=[1,2,3,4]
print(type(nam))

"""while for instantiating,we asign an object to attributes of a class"""
#create a class called Ham
class Ham():
##define the init fuction
    def __init__(self,wealth):
        self.wealth=wealth
    def eat(self):
        print("Mr ham eats less")
#Here we instantiate our object man to our class
man=Ham('very rich') 
man.eat()   
