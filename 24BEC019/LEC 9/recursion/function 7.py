def average_recursive(nums, index=0, total=0):

    if index == len(nums):
        return total / len(nums) if len(nums) > 0 else 0
    return average_recursive(nums, index + 1, total + nums[index])

my_list = [10, 20, 30, 40]
avg = average_recursive(my_list)
print("Average:", avg)
