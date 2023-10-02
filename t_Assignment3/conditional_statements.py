'''Write a Python program that prompts the user to enter their age. Depending on their age, provide the following output:
- If the age is less than 18, print "You are a minor."
- If the age is between 18 and 65 (inclusive), print "You are of working age."
- If the age is 65 or older, print "You are a senior citizen."
- If the input is invalid (e.g., not a number), print "Invalid input."
'''
def ifs():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 18:
                print("You are a minor.")
            elif 18 <= age <= 65:
                print("You are of working age.")
            else:
                print("You are a senior citizen.")
        except ValueError:
            print("Invalid input. Please enter a valid age as a number.")
ifs()