class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
        # Convert seconds to minutes
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60

        # Convert minutes to hours
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60

    def __add__(self, other):
        tot_secs = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(tot_secs)

    def __sub__(self, other):
        tot_secs = self.to_seconds() - other.to_seconds()
        if tot_secs < 0:
            tot_secs=0
        return Time.from_seconds(tot_secs)

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, tot_secs):
        hours = tot_secs // 3600
        minutes = (tot_secs % 3600) // 60
        seconds = tot_secs % 60
        return cls(hours, minutes, seconds)

    def display(self):
        print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")

if __name__ == "__main__":
    # Create two Time objects
    t1 = Time(1, 45, 50)
    t2 = Time(0, 30, 40)

    print("Time 1:")
    t1.display()

    print("Time 2:")
    t2.display()

    print("\nAfter addition:")
    t3 = t1 + t2
    t3.display()

    print("\nAfter subtraction:")
    t4 = t1 - t2
    t4.display()

    print("\nIs Time 1 less than Time 2?")
    print(t1 < t2)

    print("\nAre Time 1 and Time 2 equal?")
    print(t1 == t2)
