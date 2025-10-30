from core.player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:


    sum_value =0
    for i in hand:
        if i["rank"] >= '2' and int(i["rank"]<= '10'):
             value = int(i["rank"])
             sum_value += value
        elif  i["rank"] in ['J' ,'K'  ,'Q']:
            value = 10
            sum_value += value
        elif i["rank"] == 'A':
            value = 1
            sum_value += value

    return sum_value


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:

    for i in range(2):

       player["hand"].append(deck.pop())


    for i in range(2):


        dealer["hand"].append(deck.pop(0))



    print( calculate_hand_value(player["hand"]))
    print( calculate_hand_value(dealer["hand"]))


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value( dealer["hand"]) > 17:
        dealer["hand"].append(deck.pop())
    if calculate_hand_value( dealer["hand"]) > 21:
        print("dealer lose")
        return False
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)


    while True:
        # ask_player_action()
        a = ask_player_action()
        if a == 'H':
            player["hand"].append(deck.pop())

            if calculate_hand_value(player["hand"])> 21:
                print("you lose")
                break
        elif a == 'S':
            if not dealer_play(deck ,player):
                dealer_play(deck, player)
                break
            if dealer_play(deck ,player):
                print("you win")
                break
