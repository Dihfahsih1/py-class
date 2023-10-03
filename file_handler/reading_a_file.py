# file = open("text.txt","r")
# content=file.read()
# print(content)
# file.close()
with open("text.txt","r") as file:
    line1=file.readline()
    line2=file.readline()
    line3=file.readline()
    line4=file.readline()
print(len(line1))
    