import random
def list1():
  odd_integers = [random.choice(range(1, 100, 2)) for _ in range(5)]
  even_integers = [random.choice(range(2, 100, 2)) for _ in range(4)]
  odd_integers[2] = even_integers
  flattened_sorted_list = sorted([item for sublist in odd_integers for item in (sublist if isinstance(sublist, list) else [sublist])])
  print(flattened_sorted_list)

list1()
