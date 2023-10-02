##Using the zip function in python
nam=('name','age','school')
man='ronald',23,'progressive'

##After putting the lateral,we can asign it to any type
max=zip(nam, man)
print(dict(max))

#or we can asign it to a tuple 
print(tuple(max))
"""and this can rotate around lists,tuples,dict """
print(list(max))

##and we can also change the lateral,like
nam=('name','age','school')
man=24,23,24
x=zip(nam, man)
print(list(x))
#output
#[('name', 24), ('age', 23), ('school', 24)]

