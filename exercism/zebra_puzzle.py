''' zebra puzzle '''

nation, color, pet, bev, cigar = 'nationality', 'house color', 'animal', 'beverage', 'cigarette'

easy_hints = [
    {nation: 'English', color: 'red'},
    {nation: 'Spaniard', pet: 'dog'},
    {bev: 'coffee', color: 'green'},
    {nation: 'Ukrainian', bev: 'tea'},
    {cigar: 'Old Gold', pet: 'snails'},
    {cigar: 'Kools', color: 'yellow'},
    {cigar: 'Lucky Strike', bev: 'orange juice'},
    {nation: 'Japanese', cigar: 'Parliaments'}
]


houses = ['red', 'green', 'blue', 'ivory', 'yellow']
nations = ['English', 'Spaniard', 'Japanese', 'Norwegian', 'Ukrainian']
animals = ['dog', 'zebra', 'snails', 'horse', 'fox']
beverages = ['coffee', 'water', 'tea', 'milk', 'orange juice']
cigarettes = ['Kools', 'The Old Gold', 'Chesterfields', 'The Lucky Strike', 'Parliaments']

'''
The green house is immediately to the right of the ivory house.
The man who smokes Chesterfields lives in the house next to the man with the fox.
Kools are smoked in the house next to the house where the horse is kept.
'''

def solve():
    sol_dict = {
        1: {nation: 'Norwegian'},
        2: {color: 'blue'},
        3: {bev: 'milk'},
        4: {},
        5: {}
    }
    
    for key in sol_dict.keys():
        for help_dict in easy_hints:
            not_in_original_dict = True
            for help_key in help_dict.keys():
                if help_key in sol_dict[key].keys():
                    not_in_original_dict = False
                    break
            if not_in_original_dict:
                sol_dict[key].update(help_dict)
        print(sol_dict)
                
    print(sol_dict)
    return sol_dict

def drinks_water():
    solution = solve()
    for key in solution.keys():
        if 'water' in solution[key].items():
            return solution[key][nation]
    return 'Not Found'


def owns_zebra():
    solution = solve()
    for key in solution.keys():
        if 'zebra' in solution[key].items():
            return solution[key][nation]
    return 'Not Found'

def main():
    print(drinks_water(), 'drinks water.')
    print(owns_zebra(), 'owns zebra.')
    
if __name__ == '__main__':
    main()
