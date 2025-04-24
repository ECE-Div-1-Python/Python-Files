# 1. Find number of boys and girls in the list
def count_boys_and_girls():
    names_list = [("John", "Smith"), ("Mary", "Johnson"), ("Bob", "Brown"), ("Alice", "Davis")]
    boys_count = 0
    girls_count = 0

    for ele in names_list:
        if isinstance(ele, tuple):  # Check if the element is a tuple (boy's name in this case)
            boys_count += 1
        else:
            girls_count += 1

    print(f"Number of boys: {boys_count}, Number of girls: {girls_count}")

# 2. Create three lists for roll no., name, and age from list of tuples
def separate_student_details():
    student_list = [(1, "John", 20), (2, "Alice", 22), (3, "Bob", 19)]
    roll_no_list = [student[0] for student in student_list]
    name_list = [student[1] for student in student_list]
    age_list = [student[2] for student in student_list]

    print(f"Roll numbers: {roll_no_list}")
    print(f"Names: {name_list}")
    print(f"Ages: {age_list}")

# 3. Find the number of days between two dates
from datetime import date

def days_between_dates():
    date1 = (12, 5, 2021)  # (d, m, y)
    date2 = (25, 12, 2021)
    
    d1 = date(date1[2], date1[1], date1[0])
    d2 = date(date2[2], date2[1], date2[0])
    
    delta = d2 - d1
    print(f"Number of days between {date1} and {date2} is {delta.days} days.")

# 4. Sort food items by price in descending order
def sort_food_by_price():
    food_list = [("Pizza", 12), ("Burger", 5), ("Pasta", 8), ("Ice Cream", 3)]
    food_list.sort(key=lambda x: x[1], reverse=True)  # Sort by price in descending order
    print("Sorted food items by price (descending):", food_list)

# 5. Remove empty tuple(s) from a list of tuples
def remove_empty_tuples():
    tuple_list = [(), (1, 2), (), (3, 4), (5, 6), ()]
    filtered_list = [t for t in tuple_list if t]  # Remove empty tuples
    print("List after removing empty tuples:", filtered_list)

# 6. Modify an element of a tuple (note: tuples are immutable, but we can convert to list)
def modify_tuple():
    original_tuple = (1, 2, 3, 4, 5)
    modified_list = list(original_tuple)
    modified_list[2] = 100  # Modify the 3rd element
    modified_tuple = tuple(modified_list)
    print("Modified Tuple:", modified_tuple)

# 7. Delete an element of a tuple (again, tuples are immutable, so convert to list first)
def delete_element_from_tuple():
    original_tuple = (10, 20, 30, 40, 50)
    tuple_list = list(original_tuple)
    del tuple_list[2]  # Delete the 3rd element (index 2)
    modified_tuple = tuple(tuple_list)
    print("Tuple after deleting an element:", modified_tuple)
