# 6.	Write a program to create a class Date that has a list containing day, month and year attributes. Define an overloaded == operator to compare two Date objects.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return [self.day, self.month, self.year] == [other.day, other.month, other.year]

d1 = Date(10, 4, 2024)
d2 = Date(10, 4, 2024)
print("Dates equal:", d1 == d2)