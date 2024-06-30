import json
SCORES = [[6, 4], [9, 5], [7, 3], [8, 4], [3, 2]]
ITEMS = ["_домик_", "клубок_", "бабочка", "_миска_", "подушка", "_мышь_"]
MOUSE = [2, 6, 12, 20]
class House():
    def __init__(self):
        self.house = [["NAN", "", "", "", "NAN", ""],
                      ["", "", "", "", "NAN", ""],
                      ["NAN", "", "", "", "NAN", ""],
                      ["", "", "NAN", "", "", ""],
                      ["", "", "", "", "", ""],
                      ["", "", "", "", "", ""],
                      ["", "", "", "", "", ""]]

    def __repr__(self):
        return f"""
                      7/3
                 9/5   |   8/4
            6/4   |   6_{self.house[0][2]}_   |
             |   6_{self.house[0][1]}_   |   6_{self.house[0][3]}_
            5_{self.house[1][0]}_  |   5_{self.house[1][2]}_   |
             |   5_{self.house[1][1]}_   |   5_{self.house[1][3]}_
             |    |   4_{self.house[2][2]}_   |   3/2
             |   4_{self.house[2][1]}_   |   4_{self.house[2][3]}_   |
            3_{self.house[3][0]}_   |    |    |   3_{self.house[3][4]}_
             |   3_{self.house[3][1]}_   |   3_{self.house[3][3]}_   |
            2_{self.house[4][0]}_   |   2_{self.house[4][2]}_   |   2_{self.house[4][4]}_
             |   2_{self.house[4][1]}_   |   2_{self.house[4][3]}_   |
            1_{self.house[5][0]}_   |   1_{self.house[5][2]}_   |   1_{self.house[5][4]}_
             |   1_{self.house[5][1]}_   |   1_{self.house[5][3]}_   |
             |    |    |    |    |
             =    =    =    =    =
"""
    def score(self):
        s = 0
        s += self.score_1()
        s += self.score_2()
        s += self.score_3()
        s += self.score_4()
        s += self.score_5()
        s += self.score_6()
        return s

    def score_1(self):
        s = 0
        for i in range(5):
            w = []
            for g in range(len(self.house) - 1):
                w.append(self.house[g][i])
            if "" in w:
                s += 0
            elif 1 in w:
                s += SCORES[i][0]
            else:
                s += SCORES[i][1]
        return s

    def score_2(self):
        n = 0
        d = 0
        for i in self.house:
            d += i.count(2)
        for i in range(5):
            w = []
            for k in range(len(self.house) - 1):
                w.append(self.house[k][i])
            while 2 in w:
                a = [w.index(2), i]
                if a[1] % 2 == 0:
                    if self.house[a[0] - 1][a[1] - 1] == 2 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] - 1 <= 4:
                        n += 1
                    if self.house[a[0] - 1][a[1]] == 2 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4:
                        n += 1
                    if self.house[a[0] - 1][a[1] + 1] == 2 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] + 1 <= 4:
                        n += 1
                    if self.house[a[0]][a[1] - 1] == 2 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4:
                        n += 1
                    if self.house[a[0]][a[1] + 1] == 2 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4:
                        n += 1
                    if self.house[a[0] + 1][a[1]] == 2 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4:
                        n += 1
                else:
                    if self.house[a[0] + 1][a[1] - 1] == 2 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] - 1 <= 4:
                        n += 1
                    if self.house[a[0] - 1][a[1]] == 2 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4:
                        n += 1
                    if self.house[a[0] + 1][a[1] + 1] == 2 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] + 1 <= 4:
                        n += 1
                    if self.house[a[0]][a[1] - 1] == 2 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4:
                        n += 1
                    if self.house[a[0]][a[1] + 1] == 2 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4:
                        n += 1
                    if self.house[a[0] + 1][a[1]] == 2 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4:
                        n += 1
                w[w.index(2)] = ""
        s = d * 2 * (d - n)
        return s

    def score_3(self):
        s = 0
        for g in self.house:
            s += 3 * g.count(3)
        return s

    def score_4(self):
        s = 0
        for i in range(5):
            w = []
            for k in range(len(self.house) - 1):
                w.append(self.house[k][i])
            while 4 in w:
                a = [w.index(4), i]
                if a[1] % 2 == 0:
                    if (self.house[a[0] - 1][a[1] - 1] == 1 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 1 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] - 1][a[1] + 1] == 1 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 1 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 1 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 1 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] - 1][a[1] - 1] == 2 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 2 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] - 1][a[1] + 1] == 2 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 2 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 2 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 2 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] - 1][a[1] - 1] == 3 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 3 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] - 1][a[1] + 1] == 3 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 3 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 3 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 3 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] - 1][a[1] - 1] == 4 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 4 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] - 1][a[1] + 1] == 4 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 4 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 4 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 4 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] - 1][a[1] - 1] == 5 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 5 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] - 1][a[1] + 1] == 5 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 5 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 5 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 5 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] - 1][a[1] - 1] == 6 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 6 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] - 1][a[1] + 1] == 6 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 6 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 6 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 1 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                else:
                    if (self.house[a[0] + 1][a[1] - 1] == 1 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 1 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] + 1][a[1] + 1] == 1 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 1 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 1 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 1 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] + 1][a[1] - 1] == 2 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 2 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] + 1][a[1] + 1] == 2 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 2 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 2 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 2 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] + 1][a[1] - 1] == 3 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 3 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] + 1][a[1] + 1] == 3 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 3 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 3 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 3 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] + 1][a[1] - 1] == 4 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 4 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] + 1][a[1] + 1] == 4 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 4 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 4 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 4 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] + 1][a[1] - 1] == 5 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 5 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] + 1][a[1] + 1] == 5 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 5 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 5 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 5 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                    if (self.house[a[0] + 1][a[1] - 1] == 6 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0] - 1][a[1]] == 6 and 0 <= a[0] - 1 <= 5 and 0 <= a[1] <= 4) or (
                            self.house[a[0] + 1][a[1] + 1] == 6 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0]][a[1] - 1] == 6 and 0 <= a[0] <= 5 and 0 <= a[1] - 1 <= 4) or (
                            self.house[a[0]][a[1] + 1] == 6 and 0 <= a[0] <= 5 and 0 <= a[1] + 1 <= 4) or (
                            self.house[a[0] + 1][a[1]] == 1 and 0 <= a[0] + 1 <= 5 and 0 <= a[1] <= 4):
                        s += 1
                w[w.index(4)] = ""
        return s

    def score_5(self):
        s = 0
        for i in range(5):
            w = []
            for g in self.house:
                w.append(g[i])
            while 5 in w:
                s += 6 - w.index(5)
                w[w.index(5)] = ""
        return s

    def score_6(self):
        s = 0
        w = []
        for i in range(5):
            for k in range(6):
                if self.house[k][i] == 6:
                    a = [k, i]
                    w.append(a)
        return w
    def put(self, tower_number, floor_number, item_number):
        self.house[6-floor_number][tower_number-1]=item_number
    def save(self):
        with open('data2.json', 'w') as file:
            json.dump({"house": self.house}, file)
    def load(self):
        with open('data2.json', 'r') as file:
            s = json.load(file)
            return s["house"]

