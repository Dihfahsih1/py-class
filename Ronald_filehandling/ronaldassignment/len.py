with open("text1.txt","r") as f:
    take=f.read()
    number=len(take)
    print(number)
    f.close()