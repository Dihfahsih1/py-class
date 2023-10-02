
def reverse_func():
    '''This allows the the user to input characters and are reversed without spaces '''
    try:
        inputstr = input("Enter a sentence: ")     
        reversedstr = reversed(inputstr)
        print("".join(reversedstr))
    except ValueError:
        print("invalid input")

reverse_func()


# def my_function(x):
#   return x[::-1]

# mytxt = my_function("I wonder how this text looks like backwards")

# print(mytxt)
    
