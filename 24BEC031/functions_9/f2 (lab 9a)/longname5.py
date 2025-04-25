
fac_nms = ['Dr. Meower', 'Professor Feline', 'Bingus', 'Luna', 'Persian Shorthair', 'orange']

lng = [name for name in fac_nms if len(name) > 8]

# Print the result
print("Faculty names with more than 8 characters:")
for name in lng:
    print(name)
