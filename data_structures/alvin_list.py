def list_function():
    list1= ['physics', 'chemistry', True, 26, 1000.99]
    print('list length:', len(list1))
    list2= [80, 85, 'adult', 'age', 'salary']
    print (list1[-1])

    print ('before upate:', list1)
    list1[3] = 45
    print ('after update:', list1)

    # del list2[4]
    # print(list2)


    
list_function()