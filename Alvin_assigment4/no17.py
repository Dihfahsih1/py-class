def enume():
    lst = ['eat', 'play', 'come', 'sit']
    tple = ('here', 'you', 'go')
    strng = "AmIthereyet."

    obj1 = enumerate(lst)
    obj2 = enumerate(tple)
    obj3 = enumerate(strng)

    print(list(obj1))
    print(list(obj2))
    print(list(obj3))

    # You can also change the starting index to any index you want
    # print(list(enumerate(lst, 1)))
    # print(list(enumerate(tple, 2)))
    # print(list(enumerate(lst, 3)))
enume()