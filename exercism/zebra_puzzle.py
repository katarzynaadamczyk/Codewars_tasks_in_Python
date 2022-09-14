''' zebra puzzle '''

from copy import deepcopy

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
    def solve_r(sol, easy_num=0, advanced_num=0):
        if type(sol) == type(True) or sum([len(sol[key]) for key in sol.keys()]) == 25:
            return sol
        for i in range(easy_num, len(easy_hints)):
            for key in sol.keys():
                not_in_original_sol = True
                for hint_key in easy_hints[i].keys():
                    if hint_key in sol[key].keys():
                        not_in_original_sol = False
                        break
                if not_in_original_sol:
                    new_sol = deepcopy(sol)
                    
                    print(new_sol)
                    for hint_key in easy_hints[i].keys():
                        new_sol[key][hint_key] = easy_hints[i][hint_key]
                    solve_r(new_sol, easy_num + 1)
                    print(new_sol)
                    sol = new_sol
                    
        return sol
                
    return solve_r(sol_dict)

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
