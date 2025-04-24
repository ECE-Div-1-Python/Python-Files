class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def display(self):
        print(f"{self.date[0]:02d}-{self.date[1]:02d}-{self.date[2]}")

    def __eq__(self, other):
        return self.date == other.date

d1 = Date(22, 4, 2025)
d2 = Date(22, 4, 2025)
d3 = Date(23, 4, 2025)

print("Date 1:")
d1.display()

print("Date 2:")
d2.display()

print("Date 3:")
d3.display()

print("\nIs Date 1 equal to Date 2?", d1 == d2)
print("Is Date 1 equal to Date 3?", d1 == d3)
