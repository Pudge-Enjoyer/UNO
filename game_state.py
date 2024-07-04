class Gamestate():
    def __init__(self, players, current_player: int = 0, dices = None):
        self.players = players
        self.current_player_index = current_player
        if dices is None:
            dices = []
            for i in range(len(players)+1):
                dices.append(Dice())
        self.dices = dices

    def current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        n = len(self.players)
        self.current_player_index = (self.current_player_index + 1) % n

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