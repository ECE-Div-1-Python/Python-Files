# 8.	Implement a String class containing the following functions:
# a.	Overloaded += operator function to perform string concatenation
# b.	Method toLower() to convert upper case letters to lower case.
# c.	Method toUpper() to convert lower case letters to upper case.

class String:
    def __init__(self, content):
        self.content = content

    def __iadd__(self, other):
        self.content += other
        return self

    def toLower(self):
        self.content = self.content.lower()

    def toUpper(self):
        self.content = self.content.upper()

    def __str__(self):
        return self.content

s = String("Hello")
s += " World"
s.toUpper()
print(s)
s.toLower()
print(s)