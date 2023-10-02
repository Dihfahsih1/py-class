# USING operator.abs() METHOD and  FOR LOOP
def abso():
    list1 = [-1, 2, -67, 34, -53]
    print(list1)
    abs_list = []
    import operator
    for a in list1:
        abs_list.append(operator.abs(a))
        print(abs_list)
abso()

# USING lambda FUNCTION WITH map()
def absol():
    test_list = [9, -3, 7, -53, -2]
    # print the original list
    print("Original list is: " + str(test_list))
    # Absolute value of list elements using lambda and the map functions
    abs_func = lambda x: abs(x)
    abs_list = list(map(abs_func, test_list))
    # print the absolute list
    print("Absolute list is: " + str(abs_list))
absol()