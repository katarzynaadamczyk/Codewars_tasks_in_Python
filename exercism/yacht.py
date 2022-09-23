''' exercise yacht '''

        

# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0 
ONES = lambda dice: sum([x for x in dice if x == 1])
TWOS = lambda dice: sum([x for x in dice if x == 2])
THREES = lambda dice: sum([x for x in dice if x == 3])
FOURS = lambda dice: sum([x for x in dice if x == 4])
FIVES = lambda dice: sum([x for x in dice if x == 5])
SIXES = lambda dice: sum([x for x in dice if x == 6])
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and dice.count(dice[0]) in (2, 3) else 0
FOUR_OF_A_KIND = lambda dice: sum(set([4 * x for x in dice if dice.count(x) >= 4]))
LITTLE_STRAIGHT = lambda dice: 30 if len(set(dice)) == 5 and max(dice) == 5 else 0
BIG_STRAIGHT = lambda dice: 30 if len(set(dice)) == 5 and min(dice) == 2 else 0
CHOICE = lambda dice: sum(dice)

        
def score(dice, category):
    return category(dice)

