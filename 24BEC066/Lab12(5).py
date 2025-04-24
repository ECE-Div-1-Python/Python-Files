class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def add(self, other):
        total_sec = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_sec)

    def subtract(self, other):
        total_sec = abs(self.to_seconds() - other.to_seconds())
        return Time.from_seconds(total_sec)

    @staticmethod
    def from_seconds(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return Time(h, m, s)

t1 = Time(2, 45, 50)
t2 = Time(1, 20, 15)

print("Time 1:")
t1.display()

print("Time 2:")
t2.display()

print("\nAddition of Time:")
t3 = t1.add(t2)
t3.display()

print("\nSubtraction of Time:")
t4 = t1.subtract(t2)
t4.display()

print("\nTime 1 in seconds:", t1.to_seconds())
print("Time 2 in seconds:", t2.to_seconds())
