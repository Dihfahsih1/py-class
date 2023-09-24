##function to find average of numbers in a list''
def calculate_average():
    my_list=[1,2,3,4,5,6]
    average=sum(my_list) / 6
    print(f"the average of my_list is {average}")
calculate_average()

##Data structure manipulation"""
student_grades=[70,30,75,60,57]
average=sum(student_grades) / (5)

for x in student_grades:
    pass
else:
    print(f"The average of student_grades is {average}")
    
student_info={'mark':60,'ben':80,'stuart':67}
print(student_info)
student_info['messi']=10
print(student_info)

"""conditional statements"""
age=int(input("Enter your age: "))
if age < 18:
    print('you are a minor')
elif age <65>18:
    print('you are in working class')
elif age > 65:
    print('you are a senior citizen')
elif age !=int:
    print('Invalid input,please!!')
else:
    pass

""""While loop challenge"""
count=1 #newline
while (True):
    try:
        number=int(input('Guess the number from 1 to 100: '))
    except ValueError:
            print("Sorry come again")
            continue
    if number<17:
        print("thats lower")
        continue
    else:
        if number>17:
            print('thats higher')
            continue
        else:
            if number==17:
                print("Nice guess") 
            count=count+1   #newline
            print(f'it took you only {count} times')  
    break 

    
    

    