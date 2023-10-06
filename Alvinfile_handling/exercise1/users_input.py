import shutil
try:
    file1 = open("user_write.txt", "w")
    user_input = file1.write(input("Enter your text:\n"))
    file1.close()
    
except ValueError:
    print("no input")
