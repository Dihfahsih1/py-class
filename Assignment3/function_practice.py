def calculate_average():
    numbers = []
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    d = int(input("Enter fourth number: "))
    e = int(input("Enter fifth number: "))
    f = (a,b,c,d,e)
    f.append(numbers)
    average = sum(f) / len(f)
    print(average)
calculate_average()
