import json
from dice import Dice
def test_init():
    c = Dice()
    assert c.current_side in [1, 2, 3, 4, 5, 6]
    a = Dice(5)
    assert a.current_side == 5

def test_repr():
    c = Dice()
    assert type(c) == Dice

def test_save():
    c = Dice(3)
    assert int(c.save()) == c.current_side

def test_load():
    c = Dice(1)
    c = c.load(3)
    assert c.current_side == 3