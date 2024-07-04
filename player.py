from ai import AI
from house import House
from human import Human

class Player():
    def __init__(self, name: str, house: House = None, is_human: bool = False):
        self.name = name
        self.house_list = house
        if is_human == True:
            self.actor = Human()
        else:
            self.actor = AI()
    def __repr__(self):
        return f'{self.name}: {self.house_list}'

    def choose_dice(self, dices):
        return self.actor.choose_dice(dices)


    def choose_action(self):
        return self.actor.choose_action(self.tower_lst, self.dices)

    def to_dict(self):
        return {
            "name": self.name,
            "house": self.tower_lst.house,
            "is_human": isinstance(self.actor, Human)
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["name"], data["house"], data["is_human"])

    def save(self):
        return self.to_dict()

    @classmethod
    def load(cls, data: dict):
        cls.from_dict(data)