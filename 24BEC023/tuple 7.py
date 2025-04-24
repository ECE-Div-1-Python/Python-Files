original_tuple = (1, 2, 3, 4)
temp_list = list(original_tuple)
del temp_list[1]
modified_tuple = tuple(temp_list)

print("Original tuple:", original_tuple)
print("Tuple after deleting an element:", modified_tuple)
