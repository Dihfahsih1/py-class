comp_number = 3 - 4j
print(abs(comp_number))


user_input = input("Enter number: ")

try:
    num = float(user_input)
    result = abs(num)
    print(result)


except ValueError:
    print("invalid input")
