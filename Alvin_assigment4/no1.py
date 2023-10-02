# using the in-built reversed() function
def reverse_func():
    inputstr = input("Enter a sentence: ")
    # return the list of characters of the inputstr in reverse order
    reversedstr = reversed(inputstr)
    # then print the reversed characters without spaces.
    print("".join(reversedstr))
reverse_func()


# def my_function(x):
#   return x[::-1]

# mytxt = my_function("I wonder how this text looks like backwards")

# print(mytxt)
    
