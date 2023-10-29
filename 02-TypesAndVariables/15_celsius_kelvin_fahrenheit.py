# This one takes Celsius as a float, converts it into two(2) separate variables and then, using an f-string
# displays them in console

celsius = float(input("Temperature in Blessed Celsius: "))
kelvin = celsius + 273.15
fahrenheit = celsius*(9/5) + 32

print(f"Temperature in Peasant Kelvin: {kelvin}\nTemperature in Accursed Fahrenheit: {fahrenheit}")
