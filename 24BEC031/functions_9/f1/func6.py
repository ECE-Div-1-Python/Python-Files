def tups(end):
    
    result = [(x, x**2, x**3) for x in range(1, end + 1)]
    return result

# Example usage:
end = int(input("Enter an end value integer to print the given list: "))
tuplist = tups(end)

# Print the result
print(tuplist)
