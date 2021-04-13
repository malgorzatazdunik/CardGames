from src.Card import Card
from src.Hand import Hand


def test_add_card():
    hand = Hand()
    hand.add_card(Card("Hearts", "Two"))

    assert len(hand.cards) == 1 and hand.value == 2

def test_add_card_ace():
    hand = Hand()
    hand.add_card(Card("Clubs", "Ace"))

    assert len(hand.cards) == 1 and hand.aces == 1 and hand.value == 11


#     def adjust_for_ace(self) -> None:
#         while self.value > 21 and self.aces:
#             self.value -= 10
#             self.aces -= 1
def test_adjust_for_ace_1():
    hand = Hand()
    hand.add_card(Card("Clubs", "Ace"))
    hand.add_card(Card("Hearts", "Ace"))
    hand.add_card(Card("Spades", "Ace"))
    a = hand.value

    hand.adjust_for_ace()
    assert hand.value == a - 10 - 10

