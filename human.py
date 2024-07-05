from house_hex import House


class Human():
    def choose_dice(self, dice_list: list[int]):
        while True:
            print(dice_list)
            dice = int(input('Выберите 1 кубик: '))
            if dice in dice_list:
                return dice
            else:
                print('Такого кубика нет!')
    def choose_action(self, house: House, dices=[int, int]):
        a = f'Ваши кубики: {dices[0]}, {dices[1]}'
        while True:
            while True:
                tower = int(input('Выберите номер башни: '))
                if not(1 <= tower <= 5):
                    print('Такой башни нет!')
                    continue
                break
            while True:
                floor = int(input(f'Выберите какой кубик отвечает за этаж башни ({a}): '))
                if floor not in dices:
                    print('Такого кубика нет!')
                    continue
                break
            if dices.index(floor) == 1:
                item = dices[0]
            else:
                item = dices[1]
            if house._get(tower, floor) == "":
                return tower, floor, item
            else:
                ans = input('Сделайте другой выбор или пропустите ход \nВы хотите пропустить ход? ')
                if ans in ['да', 'Да', 'ДА', 'y', 'Y', 'Yes', 'YEs', 'YES']:
                    return None
                else:
                    continue

if __name__ == '__main__':
    c = Human()
    a = House()
    c.choose_dice([2, 4, 4])
    a.put(1, 3, 1)
    c.choose_action(a, [3, 5])