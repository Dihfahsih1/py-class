temperature = int(input("Enter the temperature value"))

if temperature > 37:
    print("It's hot outside.")
    
elif temperature <= 37:
    print("Normal human temperature")
elif temperature >= 20:
    print("It's a pleasant day.")
else:
    print("It's cold outside.")
    
