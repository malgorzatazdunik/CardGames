from Card import Card


class Hand:

    def __init__(self) -> None:
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.value += card.get_value()

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self) -> None:
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
