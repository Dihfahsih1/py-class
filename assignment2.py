def conditional():
    age = int(input("Enter your age: "))
    
    if age <= 5:
        print("You are an infant")
    elif age <= 17:
        print("You are a teenager")
    elif age >= 18:
        print("You are really old")
    else:
        print("You entered an invalid age")

conditional()