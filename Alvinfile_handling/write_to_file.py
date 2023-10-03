# file = open("me.txt", "w")
# file.write("i maah uduwd jjhfbsjk kshdb.")
# file.close()
write_to_lines = ["line 1\n", " "]
with open("me.txt", "w") as file:
    file.writelines(write_to_lines)