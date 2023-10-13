import csv
import pandas as pd
with open('sample-data.csv', 'r') as file:
    reader =csv.reader(file)
    for row in reader:
        print(row)
        
data=pd.read_csv("sample-data.csv")
print(data)

data = [["John",23,"kla"], ["Grace",30, "Mukono"], ["James",21,"Jinja"]]
with open("data.csv", 'w',newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)