from random import randrange
def build_standard_deck() -> list[dict]:

    deck = []
    suite = ["H" ,"C" ,"D" ,"S"]
    rank = ['2' ,'3' ,'4' ,'5' ,'6'  ,'7' ,'8' ,'9' ,'10' ,'J'  ,'Q' ,'K' ,'A']
    for i in suite:
        for j in rank:
            card = { "rank":j,"suite": i }
            deck.append(card)
    return deck




def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    deck = deck
    for n in range(swaps):
        a = randrange(2 ,52)
        i = deck[a]
        while True:
            b = randrange(2 ,52)
            j = deck[b]
            if j != i:
                if j["suite"] == "H":
                    if b % 5 != 0:
                        break
                elif  j["suite"] == "C" :
                    if b % 3 !=0:
                        break
                elif j["suite"]== "D" :
                    if b % 2 != 0:
                        break
                elif j["suite"]== "S":
                    if b % 7 != 0:
                        break
        deck[a] ,deck[b]= deck[b] ,deck[a]
    return deck

