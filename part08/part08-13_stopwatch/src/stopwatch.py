# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0

    def __str__(self):
        if self.seconds < 10 and self.minutes < 10:
            return f"0{self.minutes}:0{self.seconds}"
        elif self.seconds < 10:
            return f"{self.minutes}:0{self.seconds}"
        elif self.minutes < 10:
            return f"0{self.minutes}:{self.seconds}"
        else:
            return f"{self.minutes}:{self.seconds}"
