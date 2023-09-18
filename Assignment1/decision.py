average=int(input("Whats your average: "))
if average >80:
    print("excellent")
else:print("nice work buddy")
if average <60:
    print("more effort is needed buddy")

my_dict={"name":"max","age":27,"status":"single"}
my_dict["email"]="sams@gmail.com"
print(my_dict)
value=my_dict["name"]
print(value)

# while loops in python
s =1 
while s < 6:
  s += 2
  if s == 3:
          continue
  print(s)

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i= 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Understanding for loops in python
fruits=['apple','banana','orange']
for x in fruits:
  if x=='banana':
    break
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [1,2,3]:
  pass
    
    
   
    
    
    