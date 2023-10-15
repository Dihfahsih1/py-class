# file=open("text.txt","w")
# file.write("File Operations: Create, Open, Append, Read, and Write Checking File and Directory Existence Copying and Renaming Files Working with ZIP Files Exception Handling with `try`, `catch`, and `finally`")
# file.close()

lines_to_write=["line 1\n", "line 2\n", "line 3\n",]
with open("text1.txt", "w") as file:
    file.writelines(lines_to_write)