tell = input("Enter text: ")
result = tell.find("young")
print(result)
if tell.find("young") != -1:
    print("Contains substring.")
else:
    print("Doesn'tcontain substring.")