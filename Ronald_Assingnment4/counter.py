"""Counter helps us tell number of times an element repeats itself"""
##Using Counter on a string
from collections import Counter
counter=()
counter=Counter(['a','a','b','a'])
print(counter)
#using Counter on a list of elements
counter=[1,2,3,1,3,1,1,1]
counter=Counter(counter)
print(counter)