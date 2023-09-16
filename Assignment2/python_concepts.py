# TASK1. CONDITIONAL STATEMENT CHALLENGE
m = int(input("Enter your age: "))

if m >= 18:
    print ("You are an adult")
elif m > 5 < 18:
    print ("You are a minor")
elif m <= 5:
    print ("You are an infant")

else:
    print ()


# TASK2. LIST MANIPULATION
numbers = []
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
d = int(input("Fourth number: "))
e = int(input("Fifth number: "))
sum = (a + b + c + d + e)
print(sum)


# TASK4. LISTS AND ITERATION
colors = ["red", "blue", "green", "yellow", "purple"]
for a in colors:
    print(a)

def my_colors():
    colors = [["red", "blue", "green"], ["yellow", "Math", "purple"]]
    for a in range(len(colors)):
        for b in range(len(colors[a])):
            print("Index of", colors[a][b], "is", (a, b))
my_colors()


# TASK5. CALLING A FUNCTION WITHIN A FUNCTION
def square():
    m = int(input("Enter number: "))
    result = m*m
    return result
def square_and_print():
    m = int(input("Enter number: "))
    result = m*m
    print (f"The square of {m} is {result}")
    return result
    square()
square_and_print()
    

# TASK6. PARAMETERS AND ARGUMENTS
def greet():
    name = input("Enter your name: ")
    print (f"Hello {name}, how are you?")
greet()


