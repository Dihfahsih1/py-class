from scipy.constants import convert_temperature

def temperature_converter(f):
    cel_temp = convert_temperature(f, 'F', 'C')
    print(f"The {f} F is equivalent to {cel_temp} C")
    
fah_degrees =int(input("Enter ther Fer degrees to conver"))
temperature_converter(fah_degrees)