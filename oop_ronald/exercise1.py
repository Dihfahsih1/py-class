class Student:
    '''The base class for calculating the student grade depending on their age'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def calculate_grade(self):
        if self.age < 18:
            self.grade = "Minor"
        else:
            self.grade = "Adult"


# Create two Student objects and set their attributes
"""You can use the input() method to enter several inputs"""
student1 = Student("Alice", 16) 
student2 = Student("Bob", 20)

# Calculate grades for both students
student1.calculate_grade()
student2.calculate_grade()

# Print student details
print(f"Student 1: Name - {student1.name}, Age - {student1.age}, Grade - {student1.grade}")
print(f"Student 2: Name - {student2.name}, Age - {student2.age}, Grade - {student2.grade}")
