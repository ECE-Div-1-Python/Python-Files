# 5.	Write a program that creates and uses a Time class to perform various time arithmetic operations.

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        return Time(total_hours, total_minutes % 60)

    def __str__(self):
        return f"{self.hours}h {self.minutes}m"

t1 = Time(2, 45)
t2 = Time(1, 30)
print("Time Sum:", t1.add(t2))
