def  my_age():
     your_age=int(input("enter your age:"))
     if your_age >=18:
        print("you are older")
     else:
      print("you are a minor")
     if your_age <=5:
      print("you are an infant")
my_age()

def numbers(): 
   numbers=[]

   print("enter numbers of your choice")
   number_one=int(input("number one: "))
   number_two=int(input("number two: "))

   number_three=int(input("number three: "))
   number_four=int(input("number four: "))
   number_five=int(input("number five: "))

   add=(number_one + number_two + number_three)
   print(add)
   listm=(number_one,number_two,number_three)
   numbers.append(listm)
   print(numbers)
numbers()


def my_list():
    list1=["red","blue","yellow","pupple"]
    for x in list1:
        print(x)
my_list()
          
def my_list():
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
my_list()
    
    
def my_square(x):
    square=int(x*x)
    return square
my_square(6)

def sqaure_and_print(maddos):
    number=int(input("enter your number: "))
    numbers1=my_square(number)
    print(numbers1)
sqaure_and_print('maddos')
    

def greet(name):
    user_name=input("enter your name: ")
    print(f'how are you {user_name} ')
greet('user_name')


  

    

    
    
    





    



   
    

    