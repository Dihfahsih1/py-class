def my_list():
    list1 = ['physics', 'chemistry', 1997, 2000]
    list1.append("Maths")
    print("the length of the list: ", len(list1))
    print("Before Updating the list: ", list1)
    list1[-1]="Geography"
    print("After Updating the list: ", list1)
    
    del list1[-3]
    print("After deletion the list: ", list1)
    
my_list()