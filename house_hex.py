from copy import copy
SCORES = [[6, 4], [9, 5], [7, 3], [8, 4], [3, 2]]
ITEMS = ["_домик_", "клубок_", "бабочка", "_миска_", "подушка", "_мышка_"]
MOUSE = [2, 6, 12, 20]
BOT = (2, 0)
TOP = (-2, 0)
RBOT = (1, 1)
LBOT = (1, -1)
RTOP = (-1, 1)
LTOP = (-1, -1)
CONNECTIONS = [BOT, TOP, RBOT, LBOT, RTOP, LTOP]
class House():
    def __init__(self, house=None):
        if house == None:
            self.house = [["NAN", "NAN", "", "NAN", "NAN"],
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
        else:
            self.house = house

    def item(self, i, g):
        if type(self.house[i][g]) == int:
            return (ITEMS[self.house[i][g] - 1])
        else:
            return "_______"

    def __repr__(self):
        return f"""  
                                     7/3
                         9/5          |           8/4
           6/4           |         6_{self.item(0, 2)}_      |
            |         6_{self.item(1, 1)}_      |         6_{self.item(1, 3)}_
         5_{self.item(2, 0)}_      |         5_{self.item(2, 2)}_      |
            |         5_{self.item(3, 1)}_      |         5_{self.item(3, 3)}_
            |            |         4_{self.item(4, 2)}_      |           3/2
            |         4_{self.item(5, 1)}_      |         4_{self.item(5, 3)}_      |
         3_{self.item(6, 0)}_      |            |            |         3_{self.item(6, 4)}_
            |         3_{self.item(7, 1)}_      |         3_{self.item(7, 3)}_      |
         2_{self.item(8, 0)}_      |         2_{self.item(8, 2)}_      |         2_{self.item(8, 4)}_
            |         2_{self.item(9, 1)}_      |         2_{self.item(9, 3)}_      |
         1_{self.item(10, 0)}_      |         1_{self.item(10, 2)}_      |         1_{self.item(10, 4)}_
            |         1_{self.item(11, 1)}_      |         1_{self.item(11, 3)}_      |
            |            |            |            |            |
            =            =            =            =            =
        """

    def put(self, number_tower, number_floor, number_item):
        if number_tower % 2 == 1:
            if self.house[12 - 2*number_floor][number_tower - 1] != "NAN":
                if self.house[12 - 2 * number_floor][number_tower - 1] in [1, 2, 3, 4, 5, 6]:
                    print('Это место уже занято!')
                else:
                    self.house[12 - 2*number_floor][number_tower - 1] = number_item
            else:
                print(f'Такого места нет!')
        else:
            if self.house[13 - 2 * number_floor][number_tower - 1] != "NAN":
                if self.house[13 - 2 * number_floor][number_tower - 1] in [1, 2, 3, 4, 5, 6]:
                    print('Это место уже занято!')
                else:
                    self.house[13 - 2 * number_floor][number_tower - 1] = number_item
            else:
                print(f'Такого места нет!')

    def score_home1(self):
        s = 0
        for i in range(5):
            w = []
            for g in range(len(self.house)):
                w.append(self.house[g][i])
            if "" in w:
                s += 0
            elif 1 in w:
                s += SCORES[i][0]
            else:
                s += SCORES[i][1]
        return s

    def score_ball2(self):
        total_balls = 0
        total_isolated_balls = 0
        for row in range(len(self.house)):
            for col in range(len(self.house[row])):
                if self.house[row][col] != 2:
                    continue
                total_balls += 1
                isolated = True
                for connection in CONNECTIONS:
                    drow = connection[0]
                    dcol = connection[1]
                    if not self._position(row + drow, col + dcol):
                        continue
                    if self.house[row + drow][col + dcol] != 2:
                        continue
                    isolated = False
                if isolated:
                    total_isolated_balls += 1

        return total_balls * total_isolated_balls

    def score_butterfly3(self):
        s = 0
        for g in self.house:
            s += 3 * g.count(3)
        return s

    def score_bowl4(self):
        s = 0
        for row in range(len(self.house)):
            for col in range(len(self.house[row])):
                if self.house[row][col] != 4:
                    continue
                items = set()
                for connection in CONNECTIONS:
                    drow = connection[0]
                    dcol = connection[1]
                    if self._position(row + drow, col + dcol):
                        items.add(self.house[row + drow][col + dcol])
                    if "" in items:
                        items.remove("")
                    if "NAN" in items:
                        items.remove("NAN")
                s += len(set(items))
        return s


    def score_pillow5(self):
        s = 0
        for i in range(len(self.house)):
            for g in self.house[i]:
                if g == 5:
                    if self.house[i].index(g) % 2 == 0:
                        s += (12 - i)/2
                    else:
                        s += (13 - i)/2
        return s

    def score_mouse6(self):
        s = 0
        for row in range(len(self.house)):
            for col in range(len(self.house[row])):
                if self.house[row][col] != 6:
                    continue
                mice = self._find_mice_complex(row, col, [(row, col)])
                if len(mice) > 4:
                    s += 20/len(mice)
                else:
                    s += 1 + len(mice)
        return round(s)

    def score(self):
        s = 0
        s += self.score_home1()
        s += self.score_ball2()
        s += self.score_butterfly3()
        s += self.score_bowl4()
        s += self.score_pillow5()
        s += self.score_mouse6()
        return s

    def _position(self, x, y):
            if 0 <= x <= 11 and 0 <= y <= 4:
                return True
            else:
                return False


    def _find_mice_complex(self, row, col, mice):
        for drow, dcol in CONNECTIONS:
            if self._position(row + drow, col + dcol):
                if self.house[row + drow][col + dcol] != 6:
                    continue
                if (row + drow, col + dcol) in mice:
                    continue
                mice.append((row + drow, col + dcol))
                self._find_mice_complex(row + drow, col + dcol, mice)
        return mice

    def _get(self, tower, floor):
        if tower % 2 == 1:
            return self.house[12 - 2*floor][tower - 1]
        else:
            return self.house[13 - 2 * floor][tower - 1]


    def save(self):
        return self.house

    @classmethod
    def load(cls, data: list):
        return cls(data)