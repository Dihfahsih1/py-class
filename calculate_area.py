def cal_area(width, length):
    area=width * length
    return area

w=int(input("Enter width: "))
l=int(input("Enter length: "))
a = cal_area(w,l)
print(f"the area of the rectangle is {a}")