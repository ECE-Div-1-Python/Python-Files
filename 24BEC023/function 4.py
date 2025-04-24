def sum_avg(marks):
    
    if len(marks) != 5:
        raise ValueError("Exactly five marks must be provided.")
    
    total = sum(marks)
    average = total / 5  

    return total, average

marks_list = [85, 90, 78, 92, 88] 
total, average = sum_avg(marks_list)

print(f"Marks: {marks_list}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
