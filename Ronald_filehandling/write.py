file=open("text.txt","a")
content=file.write("i am married")
file.close()

file=open("mug.txt","w")

import os
if os.path.exists("mug.txt"):
    os.remove("mug.txt")
else:
    print("file doesnot exist")
    
    
def longest():
    word='Enter a sentence'
    longest=len(word)
    if longest%2==0:
        print("the word")
