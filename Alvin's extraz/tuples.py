'''UPDATING TUPLES... SNCE TUPLES ARE UNCHANGEABLE,
WE CONVERT THEM INTO LISTS THEN WE UPDATE THETHEM AND
LATER CHANGE THEM BACK TO TUPLES'''


'''CHANGING ITEM AT A GIVEN INDEX'''
# tuple1 = ("me", "you", "her")
# x = list(tuple1)
# x[-1] = "them"
# tuple1 = tuple(x)
# print(tuple1)

'''APPENDING ITEMS'''
# tuple2 = ("me", "you", "her")
# x = list(tuple2)
# x.append("his")
# tuple2 = tuple(x)
# print(tuple2)

'''DELETING A TUPLE'''
# tuple1 = ("me", "you", "her")
# del tuple1
# print(tuple1)

'''UNPACKING A TUPLE'''

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
