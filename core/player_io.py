def ask_player_action() -> str:
    ask = None
    while ask not  in ['S' , 'H']:
        ask = input("enter 'S' or 'H" )
    return ask

