from src.Chips import Chips


def test_win_bet():
    chips = Chips()
    chips.total = 100
    chips.bet = 50
    chips.win_bet()
    assert chips.total == 150


def test_lose_bet():
    chips = Chips()
    chips.total = 100
    chips.bet = 50
    chips.lose_bet()
    assert chips.total == 50
