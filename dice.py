from random import randint
class Cube():
    def __init__(self):
        self.sides=[1,2,3,4,5,6]
        self.cur_side=self.sides[randint(0,5)]

    def __repr__(self):
        return str(self.cur_side)

    def roll(self):
        return Cube()

    def save(self):
        pass

    def load(self):
        pass
