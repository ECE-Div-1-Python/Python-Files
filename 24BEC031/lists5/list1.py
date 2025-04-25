import random


odint = [random.choice(range(1, 100, 2)) for _ in range(5)]
print("Original list of odd integers:", odint)


evint = [random.choice(range(2, 100, 2)) for _ in range(4)]
print("List of even integers:", evint)

#inserting even list into odd list
odint[2] = evint
print("Odd integers after replacing the third element with the even integers:", odint)

#flat
flat = []
for item in odint:
    if isinstance(item, list):
        flat.extend(item)
    else:
        flat.append(item)
print("Flattened list:", flat)


sorted_list = sorted(flat)
print("Sorted flattened list:", sorted_list)

#was too lazy to define a func