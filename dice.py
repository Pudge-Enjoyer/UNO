from random import randint
import json
SIDES = [1, 2, 3, 4, 5, 6]
class Dice():
    def __init__(self):
        self.cur_side=SIDES[randint(0,5)]

    def __repr__(self):
        return str(self.cur_side)

    def roll(self):
        self.cur_side=SIDES[randint(0,5)]

    def save(self):
        with open('data1.json', 'w') as file:
            json.dump({"cur_side": self.cur_side}, file)
            return {"cur_side": self.cur_side}
    @staticmethod
    def load():
        with open('data1.json', 'r') as file:
            s = json.load(file)
        return s["cur_side"]
