your_age=int(input("enter your age:"))
if your_age >=18:
    print("you are older")
else:
    print("you are a minor")
if your_age <=5:
    print("you are an infant")

numbers=[]

print("enter numbers of your choice")
number_one=int(input("number one:"))
number_two=int(input("number two"))
number_three=int(input("number three"))

add=(number_one + number_two + number_three)
print(add)
listm=(number_one,number_two,number_three)
numbers.append(listm)
print(numbers)


def my_list():
    list1=["red","blue","yellow","pupple"]
    for x in list1:
        print(x)
my_list()
          

man=[[18,28,56],["men",27,"yuan"],[1,2,3]]
print(man)
man.insert(1,[2,3,4,5])
print(man)
man[1][2]="dollar"
print(man)
print(man[1][2])
for r in man:
    for c in r :
        print(c,end = " ")
    print()
    
    
def square(x=4):
    return(x*x)
print(square(4))

def sqaure_and_print(number):
    print(number)
    print(pow(8, 2))
sqaure_and_print(8)
    

def greet(name):
    print(name)
print("hello","alex")
print('hello','peter')
print('hello','mandy')


  

    

    
    
    





    



   
    

    