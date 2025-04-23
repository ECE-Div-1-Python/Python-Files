def q7():
    def sum_of_list(lst, index=0):
        if index == len(lst):
            return 0
        return lst[index] + sum_of_list(lst, index + 1)
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Average of the list is",sum_of_list(numbers)/len(numbers))
q7()