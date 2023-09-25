'''a) Create a list called `student_grades` containing the grades of 5 students (use any grades between 0 and 100).
b) Using a for loop, calculate and display the average grade of the students.
c) Create a dictionary called `student_info` where each key is a student's name and each value is their corresponding grade.
d) Add a new student to the dictionary and assign them a grade.
e) Print out the updated dictionary.
'''
# a) Create a list of student grades
student_grades = [75, 89, 92, 78, 85]

# Calculate the average grade using a for loop
total = 0
for grade in student_grades:
    total += grade
average_grade = total / len(student_grades)

# Display the average grade
print(f"Average Grade: {average_grade:.2f}")

# c) Create a dictionary of student information
student_info = {
    "Alice": 75,
    "Bob": 89,
    "Charlie": 92,
    "David": 78,
    "Eva": 85
}

# d) Add a new student and grade to the dictionary
new_student_name = "Frank"
new_student_grade = 94
student_info[new_student_name] = new_student_grade

# e) Print out the updated dictionary
print("\nUpdated Student Information:")
for name, grade in student_info.items():
    print(f"{name}: {grade}")
