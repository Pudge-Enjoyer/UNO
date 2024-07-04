from dice import Dice
from house_new import House
from player import Player
from human import Human


def test_init():
    p = Player(name='George', house=House())
    assert p.name == 'George'
    assert p.tower_lst.house == [["NAN", "NAN", "", "NAN", "NAN"],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  ["", "NAN", "", "NAN", "NAN"],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  ["NAN", "NAN", "", "NAN", "NAN"],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  ["", "NAN", "NAN", "NAN", ""],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  ["", "NAN", "", "NAN", ""],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  ["", "NAN", "", "NAN", ""],
                                  ["NAN", "", "NAN", "", "NAN"]]
def test_repr():
    a =  [["NAN", "NAN", 1, "NAN", "NAN"],
          ["NAN", "", "NAN", "", "NAN"],
          ["", "NAN", "", "NAN", "NAN"],
          ["NAN", "", "NAN", "", "NAN"],
          ["NAN", "NAN", "", "NAN", "NAN"],
          ["NAN", "", "NAN", 5, "NAN"],
          ["", "NAN", "NAN", "NAN", ""],
          ["NAN", "", "NAN", "", "NAN"],
          ["", "NAN", "", "NAN", ""],
          ["NAN", "", "NAN", "", "NAN"],
          ["", "NAN", "", "NAN", ""],
          ["NAN", 2, "NAN", "", "NAN"]]
    c = Player(name='George', house=House(a))
    print(c)

def test_choose_dice_ai():
    a = [["NAN", "NAN", 1, "NAN", "NAN"],
         ["NAN", "", "NAN", "", "NAN"],
         ["", "NAN", "", "NAN", "NAN"],
         ["NAN", "", "NAN", "", "NAN"],
         ["NAN", "NAN", "", "NAN", "NAN"],
         ["NAN", "", "NAN", 5, "NAN"],
         ["", "NAN", "NAN", "NAN", ""],
         ["NAN", "", "NAN", "", "NAN"],
         ["", "NAN", "", "NAN", ""],
         ["NAN", "", "NAN", "", "NAN"],
         ["", "NAN", "", "NAN", ""],
         ["NAN", 2, "NAN", "", "NAN"]]
    c = Player('Dimon', House(a))
    assert type(c.choose_dice([2, 4, 1])) == int
    assert c.choose_dice([2, 4, 1]) in [2, 4, 1]

def test_choose_action_ai():
    a = [["NAN", "NAN", 1, "NAN", "NAN"],
         ["NAN", "", "NAN", "", "NAN"],
         ["", "NAN", "", "NAN", "NAN"],
         ["NAN", "", "NAN", "", "NAN"],
         ["NAN", "NAN", "", "NAN", "NAN"],
         ["NAN", "", "NAN", 5, "NAN"],
         ["", "NAN", "NAN", "NAN", ""],
         ["NAN", "", "NAN", "", "NAN"],
         ["", "NAN", "", "NAN", ""],
         ["NAN", "", "NAN", "", "NAN"],
         ["", "NAN", "", "NAN", ""],
         ["NAN", 2, "NAN", "", "NAN"]]
    c = Player('Dimon', House(a))
    c.choose_action([2, 6])
    assert type(c.choose_action([2, 6])) == tuple
    assert c.choose_action([2, 6])[0] in [1, 2, 3, 4, 5]
    assert c.choose_action([2, 6])[1] in [1, 2, 3, 4, 5, 6]
    assert c.choose_action([2, 6])[2] in [1, 2, 3, 4, 5, 6]

def test_save():
    c = Player('Alex', House())
    assert c.save()['name'] == 'Alex'
    c.tower_lst.put(1, 1, 1)
    assert c.save()['house'] == [["NAN", "NAN", "", "NAN", "NAN"],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  ["", "NAN", "", "NAN", "NAN"],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  ["NAN", "NAN", "", "NAN", "NAN"],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  ["", "NAN", "NAN", "NAN", ""],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  ["", "NAN", "", "NAN", ""],
                                  ["NAN", "", "NAN", "", "NAN"],
                                  [1, "NAN", "", "NAN", ""],
                                  ["NAN", "", "NAN", "", "NAN"]]
    assert c.save()['is_human'] == False
    s = Player('Artem', House(), is_human=True)
    assert s.save()['name'] == 'Artem'
    s.tower_lst.put(1, 1, 1)
    assert s.save()['house'] == [["NAN", "NAN", "", "NAN", "NAN"],
                                 ["NAN", "", "NAN", "", "NAN"],
                                 ["", "NAN", "", "NAN", "NAN"],
                                 ["NAN", "", "NAN", "", "NAN"],
                                 ["NAN", "NAN", "", "NAN", "NAN"],
                                 ["NAN", "", "NAN", "", "NAN"],
                                 ["", "NAN", "NAN", "NAN", ""],
                                 ["NAN", "", "NAN", "", "NAN"],
                                 ["", "NAN", "", "NAN", ""],
                                 ["NAN", "", "NAN", "", "NAN"],
                                 [1, "NAN", "", "NAN", ""],
                                 ["NAN", "", "NAN", "", "NAN"]]
    assert s.save()['is_human'] == True


def test_load():
    c = Player('Alex', House())
    c.tower_lst.put(1, 1, 1)
    assert type(c.load(c.save())) == Player
    s = c.save()
    s['is_human'] = True
    assert type(c.load(s)) == Player
    assert type(c.load(s).actor) == Human
