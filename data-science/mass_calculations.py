from scipy.constants import physical_constants


height_cm=226
weight_kg=50

bmi = weight_kg/((height_cm/100)**2)
print(f"BMI is {bmi:.2f}")

if bmi <= 25:
    print("You have normal weight")
elif 26 >= bmi < 40:
    print("Overweight")
    
else:
    print("obess")
    
