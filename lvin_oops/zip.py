# 

# 
L1 = ['a', 'b', 'c', 'd', 'e']
L2 = [1, 2, 3, 4, 5]
zip_L1L2 = zip(L1,L2)
print (list(zip_L1L2))


items = ['beaans', 'potato', 'sugar', 'maize']
nums = [2, 3, 4, 7]
price = [3000, 1500, 7000, 1800]

for items, nums, price in zip(items, nums, price):
    print(f"You bought {nums} {items} for Ush.{price*nums}")