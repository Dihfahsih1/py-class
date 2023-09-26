# def loops():
#     colors = ["red", 2, True]
#     for a in colors:
#         print(a) 
# loops()

# def ran():
#     for a in range(1,6,3):
#         print(a) 
# ran()
# # LOOP BACKWARD
# def ran():
#     for a in range(6,0,-1):
#         print(a) 
# ran()

# def ran():
#     for a in list(range(6,0,-1)):
#         print(a) 
# ran()

# NESTED LOOPS
# def nested():
#     for a in range(4):
#         for b in range(5):
#             print (f"({a}, {b})")
# nested()


# USING THE ZIP FUNCTION
L1 = [1,2,3,4,5]
L2 = ['a','b','c','d','e']

zip_L1L2 = zip(L1,L2)

print(list(zip_L1L2))



from itertools import zip_longest
L1 = [1,2,3,4,5]
L2 = ['a','b','c','d']

zipL_L1L2 = zip_longest(L1,L2)

print(list(zipL_L1L2))



fruits = ["apples","oranges","bananas","melons"]
prices = [20,10,5,15]
quantities = [5,7,3,4]

for fruit, price, quantity in zip(fruits,prices,quantities):
  print(f"You bought {quantity} {fruit} for ${price*quantity}")
