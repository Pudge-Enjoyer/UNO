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
BUTTERFLY_SCORE = 3
class House():
    def __init__(self, house=None):
        if house == None:
            self.house = [["NAN", "", "NAN", "", "NAN"],
                          ["NAN", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["NAN", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "NAN", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", ""]]
        else:
            self.house = house

    def __repr__(self):
        return f"""  
                                     7/3
                         9/5          |           8/4
           6/4           |         6_{self.house[1][2]}_      |
            |         6_{self.house[0][1]}_      |         6_{self.house[0][3]}_
         5_{self.house[3][0]}_      |         5_{self.house[3][2]}_      |
            |         5_{self.house[2][1]}_      |         5_{self.house[2][3]}_
            |            |         4_{self.house[5][2]}_      |           3/2
            |         4_{self.house[4][1]}_      |         4_{self.house[4][3]}_      |
         3_{self.house[7][0]}_      |            |            |         3_{self.house[7][4]}_
            |         3_{self.house[6][1]}_      |         3_{self.house[6][3]}_      |
         2_{self.house[9][0]}_      |         2_{self.house[9][2]}_      |         2_{self.house[9][4]}_
            |         2_{self.house[8][1]}_      |         2_{self.house[8][3]}_      |
         1_{self.house[11][0]}_      |         1_{self.house[11][2]}_      |         1_{self.house[11][4]}_
            |         1_{self.house[10][1]}_      |         1_{self.house[10][3]}_      |
            |            |            |            |            |
            =            =            =            =            =
        """

    def put(self, number_tower, number_floor, number_item):
        if number_tower % 2 == 0:
            if self.house[12 - 2*number_floor][number_tower - 1] != "NAN":
                self.house[12 - 2*number_floor][number_tower - 1] = number_item
            else:
                return(f'Такого места нет!')
        else:
            if self.house[13 - 2 * number_floor][number_tower - 1] != "NAN":
                self.house[13 - 2 * number_floor][number_tower - 1] = number_item
            else:
                return(f'Такого места нет!')

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
                for connection in CONNECTIONS:
                    drow = connection[0]
                    dcol = connection[1]
                    if self._position(row + drow, col + dcol):
                        if self.house[row + drow][col + dcol] == 2:
                            continue
                total_isolated_balls += 1

        return total_balls * total_isolated_balls

    def score_butterfly3(self):
        s = 0
        for g in self.house:
            s += BUTTERFLY_SCORE * g.count(3)
        return s

    def score_bowl4(self):
        s = 0
        for row in range(len(self.house)):
            for col in range(len(self.house[row])):
                if self.house[row][col] != 4:
                    continue
                items = []
                for connection in CONNECTIONS:
                    drow = connection[0]
                    dcol = connection[1]
                    if self._position(row + drow, col + dcol):
                        items.append(self.house[row + drow][col + dcol])
                items = set(items)
                s += len(items)
        return s


    def score_pillow5(self):
        s = 0
        for i in range(len(self.house)):
            for g in self.house[i]:
                if g == 5:
                    if self.house[i].index(g) % 2 == 1:
                        s += (12 - i)/2
                    else:
                        s += (13 - i)/2
        return s

    def score_mouse6(self):
        pass

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
            if 0 <= x <= 11 and 0 <= y <= 4 :
                return True
            else:
                return False

    def save(self):
        return self.house

    @classmethod
    def load(cls, data: list):
        return cls(data)