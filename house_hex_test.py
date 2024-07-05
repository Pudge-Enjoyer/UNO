from house_hex import House

def test_position():
    c = House()
    assert c._position(2, 3) == True
    assert c._position(12, 3) == False
    assert c._position(2, -1) == False
    assert c._position(12, 12323) == False
    assert c._position(-1, -3) == False


def test_init():
    c = House()
    assert c.house == [["NAN", "NAN", "", "NAN", "NAN"],
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
    c = House()
    print(c)
    c.put(1, 1, 1)
    print(c)
    c.put(3, 3, 1)
    print(c)
    c.put(3, 2, 2)
    print(c)

def test_put():
    c = House()
    c.put(1, 1, 1)
    assert c.house[10][0] == 1
    c.put(3, 3, 1)
    assert c.house[6][2] == "NAN"
    c.put(3, 2, 2)
    assert c.house[8][2] == 2
    c.put(2, 6, 5)
    assert c.house[1][1] == 5
    c.put(2, 6, 2)
    assert c.house[1][1] == 5
    print(c)

def test_get():
    c = House()
    c.put(1, 1, 1)
    assert c._get(1, 1) == 1
    c.put(3, 3, 1)
    assert c._get(3, 3) == "NAN"
    c.put(3, 2, 2)
    assert c._get(3, 2) == 2
    c.put(2, 6, 5)
    assert c._get(2, 6) == 5
    c.put(2, 6, 2)
    assert c._get(2, 6) == 5
    print(c)

def test_score():
    c = House()
    c.put(1, 1, 1)
    c.put(1, 2, 2)
    c.put(1, 3, 3)
    c.put(1, 5, 5)
    c.put(2, 2, 4)
    c.put(2, 1, 6)
    c.put(3, 1, 6)
    c.put(4, 2, 6)
    c.put(3, 2, 4)
    c.put(2, 3, 2)
    c.put(2, 5, 5)
    c.put(2, 4, 3)
    c.put(2, 6, 2)
    c.put(5, 1, 1)
    c.put(5, 3, 5)
    c.put(4, 3, 6)
    c.put(4, 4, 6)
    print(c)
    assert c.score() == 60
def test_score_home1():
    c = House()
    assert c.score_home1() == 0
    c.put(1, 1, 1)
    assert c.score_home1() == 0
    c.put(1, 2, 2)
    c.put(1, 3, 3)
    c.put(1, 5, 5)
    assert c.score_home1() == 6
    a = House()
    assert a.score_home1() == 0
    a.put(1, 1, 2)
    assert a.score_home1() == 0
    a.put(1, 2, 2)
    a.put(1, 3, 2)
    a.put(1, 5, 2)
    assert a.score_home1() == 4

def test_score_ball2():
    c = House()
    c.put(1, 1, 2)
    assert c.score_ball2() == 1
    c.put(1, 2, 2)
    assert c.score_ball2() == 0
    c.put(5, 1, 2)
    assert c.score_ball2() == 3
    c.put(5, 3, 2)
    assert c.score_ball2() == 8
    c.put(3, 1, 2)
    assert c.score_ball2() == 15
    print(c)

def test_score_butterfly3():
    c = House()
    c.put(1, 1, 3)
    assert c.score_butterfly3() == 3
    c.put(1, 3, 3)
    assert c.score_butterfly3() == 6
    c.put(1, 2, 3)
    assert c.score_butterfly3() == 9
    c.put(1, 5, 3)
    assert c.score_butterfly3() == 12
    c.put(2, 1, 3)
    assert c.score_butterfly3() == 15
    c.put(2, 2, 3)
    assert c.score_butterfly3() == 18
    print(c)

def test_score_bowl4():
    c = House()
    c.put(3, 5, 4)
    assert c.score_bowl4() == 0
    c.put(4, 5, 1)
    assert c.score_bowl4() == 1
    c.put(3, 4, 2)
    assert c.score_bowl4() == 2
    c.put(2, 5, 3)
    assert c.score_bowl4() == 3
    c.put(2, 6, 5)
    assert c.score_bowl4() == 4
    c.put(3, 6, 6)
    assert c.score_bowl4() == 5
    c.put(4, 6, 4)
    assert c.score_bowl4() == 9
    c.put(5, 2, 4)
    assert c.score_bowl4() == 9
    c.put(5, 1, 4)
    assert c.score_bowl4() == 11
    print(c)

def test_score_pillow5():
    c = House()
    c.put(1, 1, 5)
    assert c.score_pillow5() == 1
    c.put(2, 2, 5)
    assert c.score_pillow5() == 3
    c.put(5, 3, 5)
    assert c.score_pillow5() == 6
    c.put(3, 4, 5)
    assert c.score_pillow5() == 10
    c.put(4, 5, 5)
    assert c.score_pillow5() == 15
    c.put(3, 6, 5)
    assert c.score_pillow5() == 21
    c.put(1, 2, 5)
    assert c.score_pillow5() == 23
    c.put(1, 3, 5)
    assert c.score_pillow5() == 26
    c.put(1, 5, 5)
    assert c.score_pillow5() == 31
    c.put(2, 1, 5)
    assert c.score_pillow5() == 32
    c.put(2, 3, 5)
    assert c.score_pillow5() == 35
    c.put(2, 4, 5)
    assert c.score_pillow5() == 39
    c.put(2, 5, 5)
    assert c.score_pillow5() == 44
    c.put(2, 6, 5)
    assert c.score_pillow5() == 50
    print(c)
def test_score_6():
    c = House()
    c.put(1, 1, 6)
    assert c.score_mouse6() == 2
    c.put(1, 2, 3)
    assert c.score_mouse6() == 2
    c.put(1, 3, 6)
    assert c.score_mouse6() == 4
    c.put(2, 1, 6)
    assert c.score_mouse6() == 8
    c.put(3, 1, 6)
    assert c.score_mouse6() == 14
    c.put(4, 1, 6)
    assert c.score_mouse6() == 22
    c.put(5, 1, 6)
    assert c.score_mouse6() == 22
    c.put(5, 2, 6)
    assert c.score_mouse6() == 22
    c.put(2, 4, 6)
    assert c.score_mouse6() == 26
    c.put(2, 5, 6)
    assert c.score_mouse6() == 32
    c.put(3, 4, 6)
    assert c.score_mouse6() == 40
    c.put(4, 4, 6)
    assert c.score_mouse6() == 40
    c.put(5, 3, 6)
    assert c.score_mouse6() == 20
    print(c)

def test_save():
    c = House()
    assert c.save() == c.house

def test_load():
    c = House()
    c.put(3,2,1)
    c = c.load(c.house)
    assert c.house == [["NAN", "NAN", "", "NAN", "NAN"],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["", "NAN", "", "NAN", "NAN"],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["NAN", "NAN", "", "NAN", "NAN"],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["", "NAN", "NAN", "NAN", ""],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["", "NAN", 1, "NAN", ""],
                      ["NAN", "", "NAN", "", "NAN"],
                      ["", "NAN", "", "NAN", ""],
                      ["NAN", "", "NAN", "", "NAN"]]
