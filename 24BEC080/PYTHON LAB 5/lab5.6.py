fahrenheit = list([32, 68, 77, 104, 212])
celsius = []

for temp in fahrenheit:
    c = (temp - 32) * 5/9
    celsius.append(c)

print("Temperatures in Celsius:", celsius)
