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


import pandas as pd
date=pd.DataFrame({'name':['Alice','Bob'],'age':[23,24]})
date.to_csv('data.csv',Index=False)

import csv
data=[['name','age'],['Alice',24],['mike',26]]
with open('data.csv','w',newline='') as hugged:
    datas=csv.writer(hugged)
    datas.writerows(data)
    
    
