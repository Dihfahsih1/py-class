def condi():
    Age = int(input("Enter your age: "))

    if Age < 18:
        print("You are a minor.")
    elif Age >= 18 <= 65:
        print("You are of working age.")
    elif Age > 65:
        print("You are a senior citizen.")

    elif Age.isdigit():
         Age.isdigit = int(Age)
    else:
        print("invalid input.")
condi()