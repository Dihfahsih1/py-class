#how to create a dictionery

mydict1={"name":"Johnes"}
mydict=dict(name="james", age=34, city="K'la", email="j@gmail.com")
print(mydict1)
print(mydict)




#update the dict
mydict['email']="james@gmail.com"
print(mydict)

#removing item from the dict we use pop, del

del mydict['age']
print(mydict)


#we can as well use pop
mydict.pop("email")
print(mydict)

#mergig two dicts

mydict.update(mydict1)

print(mydict)

for key,value in mydict.items():
    print(key, value)