file=open("text1.txt","r+")
line=file.readline()
print(line)
uper=line.upper()
print(uper)
print(file.write(uper))
file.close()

with open("output.txt","a+") as t:
        adds=t.write(uper)
        t.close()
        
        
with open("text1.txt","r+") as f:
    output=f.read()
    ups=output.title()
    changed=f.write(ups)
    
    f.close()
    
        
        



    

    
    
    















