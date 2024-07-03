from random import randint
import json
class Dice():
    SIDES=[1, 2, 3, 4, 5, 6]
    def __init__(self, side=None):
        if side != None and 1 <= side <= 6:
            self.cur_side = side
        else:
            self.roll()

    def __repr__(self):
        return str(self.cur_side)

    def roll(self):
        self.cur_side=self.SIDES[randint(0,5)]

    def save(self):
        return repr(self)

    @classmethod
    def load(cls, value: str):
        return cls(int(value))
