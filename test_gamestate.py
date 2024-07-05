from game_state import Gamestate
from player import Player


def test_rolled_dice():
    s = Player('Rick')
    a = Player('Morty')
    c = Gamestate([s, a], 0)
    c.rolled_dice()
    assert c.rolled_dices != c.dices
    c.rolled_dices.remove(c.rolled_dices[0])
    assert c.rolled_dices != c.dices

def test_choose_dice():
    s = Player('Rick')
    a = Player('Morty')
    c = Gamestate([s, a], 0)
    c.rolled_dice()
    c.choose_dice_stage()
    assert c.players[0].choosen_dice in [1, 2, 3, 4, 5, 6]
    assert c.players[1].choosen_dice in [1, 2, 3, 4, 5, 6]

def test_choose_action():
    s = Player('Rick')
    a = Player('Morty')
    c = Gamestate([s, a], 0)
    c.rolled_dice()
    c.choose_dice_stage()
    c.choose_action_stage()
    print(c.players[0].tower_lst)
    print(c.players[1].tower_lst)

def test_run():
    s = Player('Rick')
    a = Player('Morty')
    c = Gamestate([s, a], 0)
    c.run()