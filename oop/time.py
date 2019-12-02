class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    @property  # Getter
    def hour(self):
        return self.h

    @hour.setter  # Setter
    def hour(self, h):
        if h >= 0 and h <= 23:
            self.h = h

    @property
    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s


t = Time(10, 20, 30)
print(t.hour)
t.hour = 5
t.hour = 40
print(t.totalseconds)
