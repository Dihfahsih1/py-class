

def replace_func(text):
    original_str = "Hello, world, another world"
    updated_string=original_str.replace("world", text, 2)
    return updated_string
new_str = input("Enter new text: ")
print(f"The Update text is: {replace_func(new_str)}")