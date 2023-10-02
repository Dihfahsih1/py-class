even_numbers = []
for x in range(1, 31):
    if (lambda num: num % 2 == 0)(x):
        even_numbers.append(x)
print(even_numbers)