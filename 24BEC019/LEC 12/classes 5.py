class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        return Time(total_hours, total_minutes % 60)

    def __str__(self):
        return f"{self.hours}h {self.minutes}m"

t1 = Time(5, 45)
t2 = Time(3, 30)
print("Time Sum:", t1+t2)