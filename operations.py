def my_lists():
    my_list1=[1,3,44,5,6]
    my_list2=["man",2,4,"den"]
    my_list1.append(29)

    print(my_list1,my_list2)
    my_list1.remove(3)
    print(my_list1)
    list3=my_list1
    my_list2.remove("man")
    print(my_list2)

    list4=my_list2
    print(f'my update is {list3},and my second update is {list4}')
my_lists()
    
    
    




