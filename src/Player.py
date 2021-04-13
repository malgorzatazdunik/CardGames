from src.Card import Card


class Player:
    def __init__(self, name_: str) -> None:
        self.name = name_
        self.all_cards = []

    def remove_one(self) -> Card:
        return self.all_cards.pop(0)

    def add_cards(self, new_cards) -> None:
        if type([]) == type(new_cards):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f'Player {self.name} has {len(self.all_cards)} cards.'
