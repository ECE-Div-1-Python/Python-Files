class a:
    def __init__(self,hours,minutes,seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def standardised(self):
        if(self.seconds>59):
            count=self.seconds//60
            self.seconds%=60
            self.minutes+=count
        if(self.minutes>59):
            count=self.minutes//60
            self.minutes%=60
            self.hours+=count
        if(self.hours>23):
            self.hours%=23
        return self.hours,self.minutes,self.seconds
    def __add__(self,other):
        self.hours+=other.hours
        self.minutes+=other.minutes
        self.seconds+=other.seconds
        self.standardised()
        return self.hours,self.minutes,self.seconds
    def __sub__(self,other):
        self.hours-=other.hours
        self.minutes-=other.minutes
        self.seconds-=other.seconds
        self.standardised()
        return self.hours,self.minutes,self.seconds
current=a(4,49,40)
early=a(2,12,30)
add=current+early
print(add)