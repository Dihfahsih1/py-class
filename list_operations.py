my_list=[1,3,5,4,7,8,9]

my_list.insert(3,"number")
print(my_list)

#slicing
slicing=my_list[3]
print(slicing)

#remove
remove=my_list.pop()
print(str(remove) + "has been poped")
print(my_list)

#delete
del my_list[2]
print(my_list)

#finding an element
index = my_list.index("number")
print(index)

#checking membership
is_present= 6 in my_list
print(is_present)

