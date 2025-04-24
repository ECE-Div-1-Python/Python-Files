def q4():
    def reverse_list(lst:list):
        if len(lst) == 0:
            return []
        last = lst.pop()                 
        reversed_rest = reverse_list(lst)
        return [last] + reversed_rest      

    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    reversed_numbers = reverse_list(numbers)

    print("Reversed list:", reversed_numbers)
q4()