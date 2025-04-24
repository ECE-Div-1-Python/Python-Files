# 1. Loop chalakar har possible (a, b, c) check karna hai
# 2. Agar a^2 + b^2 == c^2, to wo ek Pythagorean Triplet hoga

print("Pythagorean Triplets with sides ≤ 30:")

# Loop chalakar a, b, c dhoondhna
for a in range(1, 31):  # a ki values 1 se 30 tak
    for b in range(a, 31):  # b ki values a se 30 tak (repeat na ho isliye a se start kiya)
        for c in range(b, 31):  # c ki values b se 30 tak
            if a**2 + b**2 == c**2:  # Pythagorean condition check
                print(f"({a}, {b}, {c})")  # Triplet print karna
