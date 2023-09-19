def loops():
    my_list=['john',45, True]
    for i in my_list:
        print(i)
loops()

def ranged():
    for i in range(1, 6):
        print(i)
ranged()

fruits=["apple", "bananas","cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
    
    
    
for i in range(len(fruits)):
    print(fruits[i])
    
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
        
count = 0
while count < 5:
    print(f"Count: {count}")
    count +=2


def while_loop():
    while True:
        my_string=input("Enter 'q' to quit: ")
        if my_string=='q':
            break
while_loop()



