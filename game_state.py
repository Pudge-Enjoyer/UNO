import json

from dice import Dice
from player import Player


class Gamestate():
    def __init__(self, players, current_player: int = 0, dices = None):
        self.players = players
        self.current_player_index = current_player
        if dices is None:
            dices = []
            for i in range(len(players)+1):
                dices.append(Dice())
        self.dices = dices

    def run(self):
        pass

    def current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        n = len(self.players)
        self.current_player_index = (self.current_player_index + 1) % n

    def rolled_dice(self):
        self.cube1 = Dice()
        self.cube2 = Dice()
        self.cube3 = Dice()
        self.lst_cubes = [self.cube1.current_side, self.cube2.current_side, self.cube3.current_side]
        return self.lst_cubes

    def choose_dice(self):
        pass

    def choose_action(self):
        pass

    def is_win_condition(self):
        for player in self.players:
            full_tower = 0
            for col in range(5):
                w = []
                for row in range(len(player.tower_lst)):
                    w.append(player.tower_lst[row][col])
                if "" not in w:
                    full_tower += 1
            if full_tower == 3:
                return True
        return False

    def win_player(self):
        lst_player = []
        for player in self.players:
            lst_player.append({
                "pl_cls": player,
                "name": player.name,
                "score": player.tower_lst.score()
            })
        sorted(lst_player, key = lambda x: x["score"])
        return f'Побеждает: {lst_player[-1]["name"]}, с количеством очков: {lst_player[-1]["score"]}'


    def save(self):
        return {
            'players': [p.save() for p in self.players],
            'current_player_index': self.current_player_index,
            'dices': [d.save() for d in self.dices]
        }
    @classmethod
    def load(cls, data):
        data = json.load(data)
        return cls([Player.load(pd) for pd in data['players']],
                   data['current_player_index'],
                   [Dice.load(dd) for dd in data['dices']])


class GameStage():
    ROLL_DICE = 1
    CHOOSE_DICE = 2
    CHOOSE_ACTION = 3
    NEXT_ROUND = 4
    END_GAME = 5
