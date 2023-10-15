# TASK1 BASIC CLASS CREATION

class Student:
    def __init__(self, Name, Age, Grade):
        self.Name = Name
        self.Age = Age
        self.Grade = Grade
    def studentGrade(self):
        if Age < 18 :
            print("Minor")
        else:
            print("Adult")

the_student = Student(Name=input("Enter student name: "), Age=int(input("Enter student age: ")), Grade=int(input("Enter student grade: ")))

print(the_student.Name)
print(the_student.Age)
print(the_student.Grade)

print(the_student.studentGrade)