temp = input("Please enter your information!!   ")
try:
    if temp != "":
        with open('gfg.txt', 'a+') as file:
            file.write(temp + "\n")
            print("Temporary saved!")
    else:
        print("you must put something")
except Exception as e:
    print("There is a Problem", str(e))