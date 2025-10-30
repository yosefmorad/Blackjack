from core import deck ,game_logic ,player_io
if __name__ == "__main__":
    new_deck = deck.build_standard_deck()


    shuffle_deck = deck.shuffle_by_suit(new_deck)

    player = {"hand": []}
    dealer = {"hand": []}

    game_logic.run_full_game(new_deck, player, dealer)



