my_name="mugabo"
name=my_name
print(str(name))

my_age=int(67)
age=my_age
print(age)

def my_life():
    name=input('what is your name:')
    age=int(input("what is your age:"))
    
    print(f'my name is {name} and am {age} years old')
my_life()

def fruits_list():
    list1=["mangoes","apples","berrys"]
    print(list1)
fruits_list()

def my_dict():
    student_info=dict(name="john",age=int(63),grade="first")
    my_dict=student_info
    for x in my_dict:
        print(x)
my_dict()