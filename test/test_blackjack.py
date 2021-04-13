import main
from src.Chips import Chips
from src.Deck import Deck
from src.Hand import Hand


# def test_something_that_involves_user_input(monkeypatch):
#
#     # monkeypatch the "input" function, so that it returns "Mark".
#     # This simulates the user entering "Mark" in the terminal:
#     monkeypatch.setattr('builtins.input', lambda _: "Mark")
#
#     # go about using input() like you normally would:
#     i = input("What is your name?")
#     assert i == "Mark"

def test_take_bet_correct(monkeypatch) -> None:
    chips = Chips()
    monkeypatch.setattr('builtins.input', lambda _: "5")
    main.take_bet(chips)
    assert chips.bet == 5


def test_check_if_exceeds_total_correct():
    exceeds = main.check_if_exceeds_total(10, 5)
    assert exceeds == True


def test_check_if_exceeds_total_incorrect():
    exceeds = main.check_if_exceeds_total(5, 10)
    assert exceeds == False


def test_hit():
    deck = Deck()
    hand = Hand()
    deck.shuffle()
    main.hit(deck, hand)
    # adjusts for ace?

    # adds card
    assert len(hand.cards) == 1


def test_hit_or_stand():
    assert False


def test_push(capsys):
    main.push()
    out, err = capsys.readouterr()
    assert out == "Dealer and Player tie! It's a push.\n"

# def dealer_wins(chips):
#     """
#     To do: Function docstring
#     """
#     print("Dealer wins!")
#     chips.lose_bet()

def test_dealer_wins(capsys):
    chips = Chips()
    main.dealer_wins()
    out, err = capsys.readouterr()

