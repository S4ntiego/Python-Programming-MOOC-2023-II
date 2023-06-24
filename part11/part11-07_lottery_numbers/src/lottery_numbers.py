from random import randint


# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, hits: list):
        self.week = week
        self.hits = hits

    def number_of_hits(self, numbers: list):
        return len([x for x in numbers if x in self.hits])

    def hits_in_place(self, numbers):
        return [x if x in self.hits else -1 for x in numbers]
