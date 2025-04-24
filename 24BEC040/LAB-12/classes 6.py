class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return [self.day, self.month, self.year] == [other.day, other.month, other.year]
    def __str__(self):
        return f"{self.day}-{self.month}-{self.year}"

d1 = Date(10, 4, 2024)
d2 = Date(10, 4, 2024)
d3 = Date(10, 6, 2007)
print('d1:',d1)
print('d2:',d2)
print('d3:',d3)

print("Dates d1 and d2 are equal:", d1 == d2)
print("Dates d1 abd d3 are equal:", d1 == d3)