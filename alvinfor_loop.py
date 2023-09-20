def loops():
    colors = ["red", 2, True]
    for a in colors:
        print(a) 
loops()

def ran():
    for a in range(1,6,3):
        print(a) 
ran()
# LOOP BACKWARD
def ran():
    for a in range(6,0,-1):
        print(a) 
ran()

def ran():
    for a in list(range(6,0,-1)):
        print(a) 
ran()

NESTED LOOPS
def nested():
    for a in range(4):
        for b in range(5):
            print (f"({a}, {b})")
nested()
