def absolute():
    try:
        n = int(float(input("Enter number: ")))
        new_n = abs(n)
        print (new_n)
    except ValueError:
        print("Do not enter text.")
absolute()