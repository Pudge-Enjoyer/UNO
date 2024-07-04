from dice import Dice
class Human():
    def choose_dice(self, dice_list: list[int]):
        while True:
            res = input('Выберите 1 кубик: ')
            dice = Dice.load(res)
            if dice in dice_list:
                dice_list.remove(dice)
                return dice
            else:
                print('Такого кубика нет!')
    def choose_action(self):
        pass