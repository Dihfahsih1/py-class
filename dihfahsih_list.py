list1 = ['physics', 'chemistry', 1997, 2000]
def my_list():
    
    for i, item in enumerate(list1):
        print(str(item) + " is at index: ", i )
    
my_list()

print("*" * 64)
#using the iterator to get the item index
def your_list():
    index=0
    for i in list1:
        print(str(i) + " is at ", index )
        index += 1
your_list()

print("*" * 64)
def ranged_list():
    for i in range(len(list1)):
        print(str(list1[i]) +" is at index ", i)
ranged_list()