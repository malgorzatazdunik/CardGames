from src.Hand import Hand
from src.Deck import Deck
from src.Chips import Chips
from src.functions import take_bet, hit, hit_or_stand, show_some, player_busts, show_all, dealer_busts, dealer_wins, \
    player_wins, push


class BlackJackClass:
    def __init__(self):
        """
        To do: Function docstring
        """

        # Create & shuffle the deck, deal two cards to each player
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_chips = Chips()  # remember the default value is 100

    def run(self):
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')
        playing = True

        while True:

            self.deck.shuffle()
            self.player_hand.add_card(self.deck.deal())
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

            # Prompt the Player for their bet
            take_bet(self.player_chips)

            # Show cards (but keep one dealer card hidden)
            show_some(self.player_hand, self.dealer_hand)

            while playing:  # recall this variable from our hit_or_stand function

                # Prompt for Player to Hit or Stand
                hit_or_stand(self.deck, self.player_hand)

                # Show cards (but keep one dealer card hidden)
                show_some(self.player_hand, self.dealer_hand)

                # If player's hand exceeds 21, run player_busts() and break out of loop
                if self.player_hand.value > 21:
                    player_busts(self.player_chips)
                    break

                    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if self.player_hand.value <= 21:

                while self.dealer_hand.value < 17:
                    hit(self.deck, self.dealer_hand)

                    # Show all cards
                show_all(self.player_hand, self.dealer_hand)

                # Run different winning scenarios
                if self.dealer_hand.value > 21:
                    dealer_busts(self.player_chips)

                elif self.dealer_hand.value > self.player_hand.value:
                    dealer_wins(self.player_chips)

                elif self.dealer_hand.value < self.player_hand.value:
                    player_wins(self.player_chips)

                else:
                    push()

                    # Inform Player of their chips total
            print("\nPlayer's winnings stand at", self.player_chips.total)

            # Ask to play again
            new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

            if new_game[0].lower() == 'y':
                playing = True
                continue
            else:
                print("Thanks for playing!")
                break
