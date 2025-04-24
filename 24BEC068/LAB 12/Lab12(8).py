class String:
    def __init__(self, text):
        self.text = text

    def __iadd__(self, other):
        self.text += other.text
        return self

    def toLower(self):
        self.text = self.text.lower()

    def toUpper(self):
        self.text = self.text.upper()

    def show(self):
        print(self.text)

s1 = String("Hello")
s2 = String(" World")

s1 += s2
print("After concatenation:")
s1.show()

s1.toLower()
print("To lowercase:")
s1.show()

s1.toUpper()
print("To uppercase:")
s1.show()
