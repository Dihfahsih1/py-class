def casing():
    try:
        name = input("Enter your name: ")
        print(name.upper())
    except ValueError:
        print("Enter text only.")
casing()