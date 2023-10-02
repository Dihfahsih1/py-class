def joining_str():
    try:
        str1 = input("enter the first: ")
        str2 = input("enter the second: ")
        # making the third string to join the two strings as one string with a space in between
        # but the join()function allows only one argument so we put the strings in a list to make it one item
        str3 = " ".join([str1, str2])
        print(str3)
    except ValueError:
        print("invalid input.")
joining_str()