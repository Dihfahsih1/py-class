def multiple():
    for i in range(1, 100):
        if i%3==0:
            print("Fizzz")
        elif i%5==0:
            print("Buzzz")
        elif i%3==0 and i%5==0:
            print("FizzzBuzzzz")
        else:
            pass
multiple()