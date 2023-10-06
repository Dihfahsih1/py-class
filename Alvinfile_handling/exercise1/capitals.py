import shutil
try:
    with open("user_write.txt", "r") as file:
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
    print("Line 1: ", line1.title())
    print("Line 2: ", line2.title())
    print("Line 3: ", line3.title())
except ValueError:
    print()