from random import randint
from random import choice
from house_new import House

items = [1, 2, 3, 4, 5, 6]
class AI():
    def choose_dice(self, dice_list: list=None):
        return choice(dice_list)

    def choose_action(self, house: House=None, dices=[int, int]):
        tower = randint(1,5)
        if house._get(tower, dices[0]) == "":
            return tower, dices[0], dices[1]
        elif house._get(tower, dices[1]) == "":
            return tower, dices[1], dices[0]
        else:
            return None
