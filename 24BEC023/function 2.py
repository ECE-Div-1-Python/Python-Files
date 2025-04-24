def compute(n):
    n_str = str(n)
    nn = int(n_str * 2)
    nnn = int(n_str * 3)
    nnnn = int(n_str * 4)
   
    result = n + nn + nnn + nnnn
    
    return result

for digit in range(4, 8):
    value = compute(digit)
    print(f"compute({digit}) = {value}")
