# def mag():
#     number=2+6j
#     ban=abs(number)
#     noun=round(ban,3)
#     print(noun)
# mag()


file=open("text.txt","r")
content=file.read()
line1=file.read('line1')
line2=file.read('line2')
print(line1, line2)
file.close()


