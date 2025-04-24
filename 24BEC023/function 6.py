def create_tuple_list(end_value):
    return [(x, x**2, x**3) for x in range(1, end_value + 1)]

ending_value = 5 
result = create_tuple_list(ending_value)

print(f"List of tuples (x, x^2, x^3) from 1 to {ending_value}:")
for item in result:
    print(item)
