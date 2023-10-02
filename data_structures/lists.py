# def list_functions():
#     list1=['physics','chemistry',1997,2000]
#     list2=[1,2,3,4,5,6,7]
#     list1[2]="math"
#     print("updated list:", list1)
#     print ("list1[0]:", list1[0])
#     print ("list2[-1:]:",list2[-1:])
# list_functions()

# def t_list():
#     list=[1,2,3,4]
#     list.append(3)
#     print(list)
# t_list()

def cal_area(length,width):
    area=length * width
    return area

length=int(input("Enter your legth"))
width=int(input("Enter your width"))
    
print(cal_area(length,width))
