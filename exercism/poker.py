
''' exercise poker '''

colors = ['S', 'D', 'H', 'C']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    
'''
STRAIGHT_FLUSH = # 5 cards in sequence, same color
FOUR_OF_A_KIND = # 4 cards with same rank, different color
FULL_HOUSE = # 3 same rank and 2 second rank, more valuable are those which are 3
FLUSH = # 5 cards of same color, not in sequence
STRAIGHT = # 5 cards in sequence, not same color
THREE_OF_A_KIND = # 3 cards of same value, not same color
TWO_PAIR = # 2 cards of one rank, 2 of other rank and the kicker
ONE_PAIR = # 2 cards of one rank, and the mix
HIGH_CARD = # ranks higher the card
''' 
# numbers added to each type of hand
SF, FK, FH, FL, ST, TK, TP, OP, HC = 10, 9, 8, 7, 6, 5, 4, 3, 2
STRAIGHT_FLUSH = lambda ranks_dict, colors_dict: SF if len(colors_dict) == 1 and (max(ranks_dict.keys()) - min(ranks_dict.keys())) == 4 else 0
FOUR_OF_A_KIND = lambda ranks_dict, colors_dict: FK if 4 in ranks_dict.values() else 0
FULL_HOUSE = lambda ranks_dict, colors_dict: FH if len(ranks_dict) == 2 and 3 in ranks_dict.values() else 0
FLUSH = lambda ranks_dict, colors_dict: FL if len(colors_dict) == 1 else 0
STRAIGHT = lambda ranks_dict, colors_dict: ST if (max(ranks_dict.keys()) - min(ranks_dict.keys())) == 4 else 0
THREE_OF_A_KIND = lambda ranks_dict, colors_dict: TK if len(ranks_dict) == 3 and 3 in ranks_dict.values() else 0
TWO_PAIR = lambda ranks_dict, colors_dict: TP if len(ranks_dict) == 3 and 2 in ranks_dict.values() else 0
ONE_PAIR = lambda ranks_dict, colors_dict: OP if len(ranks_dict) == 4 else 0
HIGH_CARD = lambda ranks_dict, colors_dict: HC



def score(hand):
    hand_ranks, hand_colors = [ranks.index(card[:-1]) for card in hand], [card[-1] for card in hand]
    ranks_dict = {x: hand_ranks.count(x) for x in hand_ranks}
    colors_dict = {x: hand_colors.count(x) for x in hand_colors}
    print(ranks_dict)
    print(colors_dict)
    return 0

def best_hands(hands):
    if len(hands) < 1:
        raise ValueError('wrong number of hands')
    if len(hands) == 1:
        return [hands[0]]
    scores = [score(hand.split()) for hand in hands]
    max_score = max(scores)
    return [hands[index] for index, value in enumerate(scores) if value == max_score]
   

def main():
    print(best_hands(["4H 6H 7H 8H 5H", "5S 7S 8S 9S 6S"]))
    print('should equal ["5S 7S 8S 9S 6S"]')
    
    
if __name__ == '__main__':
    main()
    
