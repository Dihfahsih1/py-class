# TASK1. CONDITIONAL STATEMENT CHALLENGE
def condition():
    m = int(input("Enter your age: "))

    if m >= 18:
        print ("You are an adult")
    elif m > 5 < 18:
        print ("You are a minor")
    elif m <= 5:
        print ("You are an infant")
condition()


# TASK2. LIST MANIPULATION
def add():
    numbers = []
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    d = int(input("Fourth number: "))
    e = int(input("Fifth number: "))
    f = (a,b,c,d,e)
    numbers.append(f)
    print (numbers)
    sum = (a + b + c + d + e)
    print(sum)
    
add()

# TASK4. LISTS AND ITERATION
colors = ["red", "blue", "green", "yellow", "purple"]
for a in colors:
    print(a)

def my_colors():
    colors = [["red", "blue", "green"], ["yellow", "Math", "purple"]]
    for a in enumerate(colors, 100):
        print(a)
    for count, a in enumerate(colors, 100):
        print(count, a)
    for count, a in enumerate(colors):
        print(count)
        print(a)
my_colors()


# TASK5. CALLING A FUNCTION WITHIN A FUNCTION
def square(number):
    return number*number
def square_and_print(b):
    return (square(b))
number = int(input("Enter number: "))
print(f"The square of{number} is {square()}")
    

# TASK6. PARAMETERS AND ARGUMENTS
def greet(name):
    return name 
name = input("Enter your name: ")
print(f"Hello {name}, you are welcome.")


