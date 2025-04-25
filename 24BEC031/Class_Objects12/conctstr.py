class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        return self

    def toLower(self):
        self.value = self.value.lower()
        return self

    def toUpper(self):
        self.value = self.value.upper()
        return self

    def display(self):
        print(self.value)

if __name__ == "__main__":

    str1 = String("MIAU")
    str2 = String("MAO")

    print("String 1: ", end="")
    str1.display()

    print("String 2: ", end="")
    str2.display()

    str1 += str2
    print("\nAfter concatenation (str1 += str2): ", end="")
    str1.display()

    str1.toLower()
    print("\nAfter converting to lowercase: ", end="")
    str1.display()

    str1.toUpper()
    print("\nAfter converting to uppercase: ", end="")
    str1.display()
