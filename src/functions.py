from src.Hand import Hand
from src.Deck import Deck
from src.Chips import Chips

def take_bet(chips : Chips) -> None:
    """
    To do: Function docstring
    """

    while True:
        try:
            chips.bet = take_bet_input()
        except ValueError:
            print('Must input integer')
        else:
            if check_if_exceeds_total(chips.bet, chips.total):
                print(f"Can't exceed {chips.total}")
            else:
                break


def take_bet_input() -> int:
    """
    To do: Function docstring
    """
    ans = int(input('How many chips would you like to bet? '))
    return ans


def check_if_exceeds_total(bet: int, total: int) -> bool:
    """
    To do: Function docstring
    """
    if bet > total:
        return True
    return False


def hit(deck_: Deck, hand: Hand) -> None:
    """
    To do: Function docstring
    """
    hand.add_card(deck_.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck_: Deck, hand: Hand) -> None:
    """
    To do: Function docstring
    """
    global playing  # to control an upcoming while loop
    while True:
        user_input: str = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if user_input[0].lower() == 'h':
            hit(deck_, hand)  # hit() function defined above

        elif user_input[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    """
    To do: Function docstring
    """
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    """
    To do: Function docstring
    """
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(chips: Chips):
    """
    To do: Function docstring
    """
    print("Player busts!")
    chips.lose_bet()


def player_wins(chips: Chips):
    """
    To do: Function docstring
    """
    print("Player wins!")
    chips.win_bet()


def dealer_busts(chips):
    """
    To do: Function docstring
    """
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(chips):
    """
    To do: Function docstring
    """
    print("Dealer wins!")
    chips.lose_bet()


def push():
    """
    To do: Function docstring
    """
    print("Dealer and Player tie! It's a push.")
