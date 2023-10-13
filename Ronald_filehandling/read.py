file=open("text.txt","r")
for massive in file:
    print(massive)
    

print(file.readline())
print(file.readline())
print(file.readline())
file.close()