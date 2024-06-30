from house import House
import json
def test_score():
    c = House()
    c.put(1, 1, 1)
    c.put(1, 2, 2)
    c.put(1, 3, 3)
    c.put(1, 5, 5)
    c.score()==16

def test_score_1():
    c = House()
    assert c.score_1() == 0
    c.put(1, 1, 1)
    assert c.score_1() == 0
    c.put(1, 2, 2)
    c.put(1, 3, 3)
    c.put(1, 5, 5)
    assert c.score_1() == 6
    a = House()
    assert a.score_1() == 0
    a.put(1, 1, 2)
    assert a.score_1() == 0
    a.put(1, 2, 2)
    a.put(1, 3, 2)
    a.put(1, 5, 2)
    assert a.score_1() == 4
    assert type(a.score_1()) == int

def test_score_2():
    c = House()
    c.put(1, 1, 2)
    assert c.score_2() == 2
    c.put(1, 2, 2)
    assert c.score_2() == 0
    c.put(5, 1, 2)
    assert c.score_2() == 6
    c.put(5, 3, 2)
    assert c.score_2() == 16

def test_score_3():
    c = House()
    c.put(1, 1, 3)
    assert c.score_3() == 3
    c.put(1, 3, 3)
    assert c.score_3() == 6
    c.put(1, 2, 3)
    assert c.score_3() == 9
    c.put(1, 5, 3)
    assert c.score_3() == 12
    c.put(2, 1, 3)
    assert c.score_3() == 15
    c.put(2, 2, 3)
    assert c.score_3() == 18
    print(c)

def test_score_4():
    c = House()
    c.put(3, 5, 4)
    assert c.score_4() == 0
    c.put(4, 5, 1)
    assert c.score_4() == 1
    c.put(3, 4, 2 )
    assert c.score_4() == 2
    c.put(2, 5, 3)
    assert c.score_4() == 3
    c.put(2, 6, 5)
    assert c.score_4() == 4
    c.put(3, 6, 6)
    assert c.score_4() == 5
    c.put(4, 6, 4)
    assert c.score_4() == 9
    c.put(5, 2, 4)
    assert c.score_4() == 9
    c.put(5, 1, 4)
    assert c.score_4() == 11
    print(c)

def test_score_5():
    c = House()
    c.put(1, 1, 5)
    assert c.score_5() == 1
    c.put(2, 2, 5)
    assert c.score_5() == 3
    c.put(5, 3, 5)
    assert c.score_5() == 6
    c.put(3, 4, 5)
    assert c.score_5() == 10
    c.put(4, 5, 5)
    assert c.score_5() == 15
    c.put(3, 6, 5)
    assert c.score_5() == 21
    c.put(1, 2, 5)
    assert c.score_5() == 23
    c.put(1, 3, 5)
    assert c.score_5() == 26
    c.put(1, 5, 5)
    assert c.score_5() == 31
    c.put(2, 1, 5)
    assert c.score_5() == 32
    c.put(2, 3, 5)
    assert c.score_5() == 35
    c.put(2, 4, 5)
    assert c.score_5() == 39
    c.put(2, 5, 5)
    assert c.score_5() == 44
    c.put(2, 6, 5)
    assert c.score_5() == 50
    print(c)
def test_score_6():
    c = House()
    c.put(1, 1, 6)
    print(c.score_6())

def test_save():
    c = House()
    c.save()
    with open('data2.json', 'r') as file:
        a = json.load(file)
    assert a == {"house":c.house}
    assert type(a) == dict

def test_load():
    c = House()
    c.save()
    assert c.load() == c.house