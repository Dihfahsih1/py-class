def calculate_average(numbers):
    '''Write a Python function called `calculate_average`
    that takes a list of numbers as input and returns their average.
    Test the function with a list of numbers provided by the instructor.'''
    if len(numbers) == 0:
        return 0  # Return 0 for an empty list to avoid division by zero
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Test the function
sample_grades = [85, 90, 78, 92, 88]
average_grade = calculate_average(sample_grades)
print(f"Average Grade: {average_grade:.2f}")