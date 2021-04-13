class Card:
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10,
              'Queen': 10, 'King': 10, 'Ace': 11}

    values_war = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 11,
              'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, suit_: str, rank_: str) -> None:
        self.suit = suit_
        self.rank = rank_
        self.value = Card.values[rank_]
        self.value_war = Card.values_war[rank_]

    def get_value(self) -> int:
        return self.value

    def get_value_war(self) -> int:
        return self.values_war

    def __str__(self) -> str:
        return self.rank + " of " + self.suit
