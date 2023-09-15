# CONDITIONAL STATEMENT CHALLENGE
m = int(input("Enter your age: "))

if m >= 18:
    print ("Your are an adult")
elif m > 5 < 18:
    print ("You are a minor")
elif m <= 5:
    print ("You are an infant")

else:
    print ()


# LIST MANIPULATION
numbers = []
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
d = int(input("Fourth number: "))
e = int(input("Fifth number: "))
sum = (a + b + c + d + e)
print(sum)


# LISTS AND ITERATION
colors = ["red", "blue", "green", "yellow", "purple"]
for a in colors:
    print(a)

def my_colors():
    colors = [["red", "blue", "green"], ["yellow", "Math", "purple"]]
    for a in range(len(colors)):
        for b in range(len(colors[a])):
            print("Index of", colors[a][b], "is", (a, b))
my_colors()


# 

