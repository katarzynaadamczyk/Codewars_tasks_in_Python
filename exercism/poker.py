
''' exercise poker '''

types = ['S', 'D', 'H', 'C']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    
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

def score(hand):
    return 0

def best_hands(hands):
    if len(hands) < 1:
        raise ValueError('wrong number of hands')
    if len(hands) == 1:
        return [hands[0]]
    scores = [score(hand) for hand in hands]
    max_score = max(scores)
    return [hands[index] for index, value in enumerate(scores) if value == max_score]
   

def main():
    print(best_hands(["4H 6H 7H 8H 5H", "5S 7S 8S 9S 6S"]))
    print('should equal ["5S 7S 8S 9S 6S"]')
    
    
if __name__ == '__main__':
    main()
    
