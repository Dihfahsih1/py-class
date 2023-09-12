def greet(name:bool, age:int):
    '''This a hello world function'''
    return "Hello "  + name + "-" + age + " years old"

#the order of the arguements matters
print(greet(False, int("this ther")))