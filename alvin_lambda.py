def lam():
    even = lambda x : x%2 == 0
    print(even)
    if even == True:
        for a in range(1, 30):
            if a <= 30:
                print(a)
lam()



# USING ONE LINE OF CODE
# even = list(filter(lambda x: x%2 == 0, range(1, 31)))
# print(even)