# file = open("me.txt", "r")
# content = file.read()
# print(content)
# file.close()

with open("me.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()
    line4 = file.readline()
print("Line 1: ", line1)
print("Line 2: ", line2)
print("Line 3: ", line3)
print("Line 4: ", line4)