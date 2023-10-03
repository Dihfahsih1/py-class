temp = input("Please enter your information!!   ")
try:
    if temp != "":
        with open('gfg.txt', 'a+') as gfg:
            gfg.write(temp + "\n")
            print("Temporary saved!")
    print("you must put something")
except Exception as e:
    print("There is a Problem", str(e))