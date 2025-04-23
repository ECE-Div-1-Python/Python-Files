def sanitize(lst):
    if not lst:
        return []
    return [max(lst[0], 0)] + sanitize(lst[1:])
lst = [-5,-4,-3,-2,-1,0,1, 2, 3, 4, 5, 6, 7, 8]
print(sanitize(lst))