def square(number):
    return number * number

def square_and_print(x):
    return(square(x))
   
your_input=int(input("Enter the number to square: "))
print(f"the square of {your_input} is: ", square_and_print(your_input))