count = 0
while count < 5:
    print (f"count: {count}") 
    count +=5

def wile():
    enter = input("developer: ")
    while enter == "developer" :
        print(f"Developer exists in {enter}")
        break
wile()

def my_colors():
    colors = ["red", "blue", "green"]
    for a in enumerate(colors):
        print(a)
my_colors()

def loop():
    while True:
        m = input("Enter 'a' to stop: ")
        if m == 'a':
            break
loop()