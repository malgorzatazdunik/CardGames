import blackjack
import pytest
import module
from Chips import Chips


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
    blackjack.take_bet(chips)
    assert chips.bet == 5


# def test_raises():
#     with pytest.raises(Exception) as execinfo:
#         raise Exception('some info')
#     # these asserts are identical; you can use either one
#     assert execinfo.value.args[0] == 'some info'
#     assert str(execinfo.value) == 'some info'

# def test_take_bet_incorrect(monkeypatch) -> None:
#     chips = Chips()
#     monkeypatch.setattr('builtins.input', lambda _: "gosia")
#
#     with pytest.raises(TypeError) as error:
#         blackjack.take_bet(chips)
#
#     assert str(error.value) == 'some info'


def test_take_bet_input_incorrect(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "gosia")
    with pytest.raises(ValueError) as error:
        blackjack.take_bet_input()

    assert str(error.value) == 'Must input integer'


def test_hit():
    assert False


