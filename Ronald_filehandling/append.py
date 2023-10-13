#for open
file=open("text.txt","r")
print(file.read())
file.close()
##dealing with read filehandler
file=open("text.txt","r")
print(file.readline())
print(file.readline())
file.close()
"""appending a sentence to the file"""
file=open("text.txt","a")
content=file.write("\ni am bone")
file.close()

file=open("text.txt","w")
content=file.write("i am born")
file.close()

import os
if os.path.exists("man.txt"):
	os.remove("man.txt")
else:
  	print("file doesnot exist")