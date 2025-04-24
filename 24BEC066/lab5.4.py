import random


odd = random.sample(range(1, 100, 2), 5)
even = random.sample(range(2, 100, 2), 4)
odd[2] = even
flat = [x for i in odd for x in (i if isinstance(i, list) else [i])]
print("Sorted List:", sorted(flat))


nums = [random.randint(1, 50) for _ in range(20)]
n = int(input("Enter number: "))
pos = [i for i, x in enumerate(nums) if x == n]
print("Positions:", pos if pos else "Not found")


nums_50 = list(set(random.randint(1, 30) for _ in range(50)))
print("Unique numbers:", nums_50)


nums_30 = [random.randint(-50, 50) for _ in range(30)]
pos_nums = [x for x in nums_30 if x > 0]
neg_nums = [x for x in nums_30 if x < 0]
print("Positive:", pos_nums)
print("Negative:", neg_nums)
