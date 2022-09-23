
''' exercise poker '''

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# numbers added to each type of hand
SF1, SF, FK, FH, FL, ST1, ST, TK, TP, OP, HC = 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
STRAIGHT_FLUSH_WITH_ACE_AS_ONE = lambda ranks_dict, colors_dict: SF1 if len(colors_dict) == 1 and \
                                                                    sorted(list(ranks_dict.keys())) == [0, 1, 2, 3, 12] else 0
STRAIGHT_FLUSH = lambda ranks_dict, colors_dict: SF if len(colors_dict) == 1 and \
                                                    (max(ranks_dict.keys()) - min(ranks_dict.keys())) == 4 else 0
FOUR_OF_A_KIND = lambda ranks_dict, colors_dict: FK if 4 in ranks_dict.values() else 0
FULL_HOUSE = lambda ranks_dict, colors_dict: FH if len(ranks_dict) == 2 and 3 in ranks_dict.values() else 0
FLUSH = lambda ranks_dict, colors_dict: FL if len(colors_dict) == 1 else 0
STRAIGHT_WITH_ACE_AS_ONE = lambda ranks_dict, colors_dict: ST1 if len(ranks_dict) == 5 and \
                                                              sorted(list(ranks_dict.keys())) == [0, 1, 2, 3, 12] else 0
STRAIGHT = lambda ranks_dict, colors_dict: ST if len(ranks_dict) == 5 and \
                                              (max(ranks_dict.keys()) - min(ranks_dict.keys())) == 4 else 0
THREE_OF_A_KIND = lambda ranks_dict, colors_dict: TK if len(ranks_dict) == 3 and 3 in ranks_dict.values() else 0
TWO_PAIR = lambda ranks_dict, colors_dict: TP if len(ranks_dict) == 3 and 2 in ranks_dict.values() else 0
ONE_PAIR = lambda ranks_dict, colors_dict: OP if len(ranks_dict) == 4 else 0
HIGH_CARD = lambda ranks_dict, colors_dict: HC

category = [STRAIGHT_FLUSH_WITH_ACE_AS_ONE, STRAIGHT_FLUSH, FOUR_OF_A_KIND, FULL_HOUSE, FLUSH, 
            STRAIGHT_WITH_ACE_AS_ONE, STRAIGHT, THREE_OF_A_KIND, TWO_PAIR, ONE_PAIR, HIGH_CARD]

def score(hand):
    hand_ranks, hand_colors = [ranks.index(card[:-1]) for card in hand], [card[-1] for card in hand]
    ranks_dict = {x: hand_ranks.count(x) for x in hand_ranks}
    colors_dict = {x: hand_colors.count(x) for x in hand_colors}
    hand_category = 0
    for cat in category:
        hand_category = cat(ranks_dict, colors_dict)
        if hand_category > 0:
            break
    if hand_category in [SF1, ST1]:
        hand_category -= 1
        ranks_dict[-1] = ranks_dict.pop(12)
    return hand_category, sorted(list(ranks_dict.keys()), key=lambda x: (ranks_dict[x], x), reverse=True)

def best_hands(hands):
    if len(hands) < 1:
        raise ValueError('wrong number of hands')
    if len(hands) == 1:
        return [hands[0]]
    scores, sorted_hands = [], []
    for hand in hands:
        hand_score, lst_of_cards = score(hand.split())
        scores.append(hand_score)
        sorted_hands.append(lst_of_cards)
    max_score = max(scores)
    print(scores)
    print(sorted_hands)
    max_values = [index for index, value in enumerate(scores) if value == max_score]
    max_cards = max([sorted_hands[index] for index in max_values])
    return [hands[index] for index, value in enumerate(sorted_hands) if value == max_cards]
   
   
def main():
    print(best_hands(["4H 6H 7H 8H 5H", "5S 7S 8S 9S 6S"]))
    print('should equal ["5S 7S 8S 9S 6S"]')
    print(best_hands(["2S 8H 2D 8D 3H", "4S 5H 4C 8S 5D"]))
    print('should equal ["2S 8H 2D 8D 3H"]')
    print(best_hands(["4S 5H 4C 8D 4H", "4D AH 3S 2D 5C"]))
    print('should equal ["4D AH 3S 2D 5C"]')
    
    
    
if __name__ == '__main__':
    main()
    
