def reverse_list(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse_list(lst))