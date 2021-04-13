from src.Deck import Deck
from src.Player import Player

if __name__ == '__main__':

    player_one = Player("One")
    player_two = Player("Two")

    new_deck = Deck()
    new_deck.shuffle()

    for i in range(26):
        player_one.add_cards(new_deck.deal())
        player_two.add_cards(new_deck.deal())

    # print(len(player_one.all_cards))
    # print(len(player_two.all_cards))
    game_in_progress = True

    round_num = 0
    while game_in_progress:
        round_num += 1
        print()
        print(f"Round {round_num} \n")

        if len(player_one.all_cards) == 0:
            print("Player two wins")
            game_in_progress = False
            break

        if len(player_two.all_cards) == 0:
            print("Player one wins")
            game_in_progress = False
            break

        p1_cards_in_play = [player_one.remove_one()]

        p2_cards_in_play = [player_two.remove_one()]

        at_war = True

        while at_war:
            print(f"{p1_cards_in_play[-1].value_war} vs {p2_cards_in_play[-1].value_war}")

            if p1_cards_in_play[-1].value_war > p2_cards_in_play[-1].value_war:
                player_one.add_cards(p1_cards_in_play)
                player_one.add_cards(p2_cards_in_play)
                print("Player one wins round")
                at_war = False

            elif p2_cards_in_play[-1].value_war > p1_cards_in_play[-1].value_war:
                player_two.add_cards(p2_cards_in_play)
                player_two.add_cards(p1_cards_in_play)
                print("Player two wins round")
                at_war = False

            else:
                print()
                print('War! \n')

                if len(player_one.all_cards) < 5:
                    print("Player one doesn't have enough cards to declare war")
                    print("Player two wins")
                    game_in_progress = False
                    break

                elif len(player_two.all_cards) < 5:
                    print("Player two doesn't have enough cards to declare war")
                    print("Player one wins")
                    game_in_progress = False
                    break

                else:
                    for i in range(5):
                        print(f"{p1_cards_in_play[-1].value_war} vs {p2_cards_in_play[-1].value_war}")
                        p1_cards_in_play.append(player_one.remove_one())
                        p2_cards_in_play.append(player_two.remove_one())
