def input_func():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

def output_func():
    user_name, user_age = input_func()
    print(f"Your name is: {user_name} and your age is: {user_age}")

output_func()

def print_block():
    text = "A more pythonic function"
    text_lines = text.split('\n')
    max_line_length = max(len(line) for line in text_lines)
    
    block = []
    block.append('*' * (max_line_length + 8))
    
    for line in text_lines:
        block_line = f'*    {line}{" " * (max_line_length - len(line))}    *'
        block.append(block_line)
    
    block.append('*' * (max_line_length + 8))
    
    for line in block:
        print(line)

print_block()

def input_func():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

def output_func(user_name, user_age):
    print(f"Your name is: {user_name} and your age is: {user_age}")

# Capture the values returned by input_func and pass them to output_func
user_name, user_age = input_func()
output_func(user_name, user_age)

    