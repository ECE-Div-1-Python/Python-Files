class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.date == other.date
        return False

    def display(self):
        print(f"{self.date[0]}/{self.date[1]}/{self.date[2]}")

if __name__ == "__main__":

    d1 = Date(15, 8, 2025)
    d2 = Date(15, 8, 2025)
    d3 = Date(1, 1, 2023)

    print("Date 1: ", end="")
    d1.display()

    print("Date 2: ", end="")
    d2.display()

    print("Date 3: ", end="")
    d3.display()

    print("\nIs Date 1 equal to Date 2?")
    print(d1 == d2)
    print("\nIs Date 1 equal to Date 3?")
    print(d1 == d3)
