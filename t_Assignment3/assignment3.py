##function to find average of numbers in a list''
def calculate_average():
    my_list=[1,2,3,4,5,6]
    average=sum(my_list) / 6
    print(f"the average of my_list is {average}")
calculate_average()

##Data structure manipulation"""
student_grades=[70,30,75,60,57]
average=sum(student_grades) / len(student_grades)

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

import random
1
guess_number=random.randint(1, 5)
attempts=0
while True:
    guess=int(input("whats the number (1-100):"))
    attempts += 1
    
    if guess < guess_number:
        print("Higher! Try again.")
    elif guess > guess_number:
        print("Lower! Try again.")
    else:
        print(f"Congratulations! You guessed number {guess_number} in {attempts} attempts.")
        break
    
