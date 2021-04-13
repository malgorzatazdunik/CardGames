from src.Card import Card
import random


class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
             'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self) -> None:
        self.deck = []

        for suit in Deck.suits:
            for rank in Deck.ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def deal(self) -> Card:
        return self.deck.pop()
