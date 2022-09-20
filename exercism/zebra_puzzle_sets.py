''' zebra puzzle solved on sets '''

from copy import deepcopy
from functools import reduce

colors = {'red', 'green', 'blue', 'ivory', 'yellow'}
nations = {'English', 'Spaniard', 'Japanese', 'Norwegian', 'Ukrainian'}
animals = {'dog', 'zebra', 'snails', 'horse', 'fox'}
beverages = {'coffee', 'water', 'tea', 'milk', 'orange juice'}
cigarettes = {'Kools', 'The Old Gold', 'Chesterfields', 'The Lucky Strike', 'Parliaments'}

all = [colors, nations, animals, beverages, cigarettes]

easy_hints = [
    {'English', 'red'},
    {'Spaniard', 'dog'},
    {'coffee', 'green'},
    {'Ukrainian', 'tea'},
    {'Old Gold', 'snails'},
    {'Kools', 'yellow'},
    {'Lucky Strike', 'orange juice'},
    {'Japanese', 'Parliaments'}
]

# The green house is immediately to the right of the ivory house.
def green_ivory_hint(all_solutions):
    new_solutions = []
    for solution in all_solutions:
        for index, house in enumerate(solution):
            if index < (len(solution) - 1) and (house & colors) == set() == (solution[index + 1] & colors):
                new_solution = deepcopy(solution)
                new_solution[index].add('green')
                new_solution[index + 1].add('ivory')
                new_solutions.append(new_solution)
    return new_solutions

# The man who smokes Chesterfields lives in the house next to the man with the fox.
# Kools are smoked in the house next to the house where the horse is kept.
def animal_cigarette_hint(all_solutions):
    animal_cigar = [['fox', 'Chesterfields'], ['horse', 'Kools']]
    new_solutions = []
    for animal, cigar in animal_cigar:
        for solution in all_solutions:
            for index, house in enumerate(solution):
                if index > 0 and (house & animals == set()) and (solution[index - 1] & cigarettes) == set():
                    new_solution = deepcopy(solution)
                    new_solution[index].add(animal)
                    new_solution[index - 1].add(cigar)
                    new_solutions.append(new_solution)
                if index < len(solution) - 1 and (house & animals == set()) and (solution[index + 1] & cigarettes) == set():
                    new_solution = deepcopy(solution)
                    new_solution[index].add(animal)
                    new_solution[index + 1].add(cigar)
                    new_solutions.append(new_solution)
        all_solutions = new_solutions
        new_solutions = []
    return all_solutions


def solution_union(solution):
    return reduce(lambda x, y: x.union(y), solution)


def easy_hints_adder(all_solutions):
    new_solutions = []
    for trait1, trait2 in easy_hints:
        # find niche of traits
        pass
    return all_solutions


def print_all_solutions(all_solutions):
    for index, solution in enumerate(all_solutions):
        print(index, ":")
        for house_number, values in enumerate(solution):
            print(house_number, ":", values)
        print()


def solve():
    solution = [set(), set(), set(), set(), set()]
    solution[0].add('Norwegian')
    solution[1].add('blue')
    solution[2].add('milk')
    all_solutions = [solution]
    all_solutions = green_ivory_hint(all_solutions)
    all_solutions = animal_cigarette_hint(all_solutions)
    print_all_solutions(all_solutions)
    # TODO
    
    
    return solution


def drinks_water():
    solution = solve()
    for item in solution:
        if 'water' in item:
            return list(item.intersection(nations))[0]
    return 'Not Found'


def owns_zebra():
    solution = solve()
    for item in solution:
        if 'zebra' in item:
            return list(item.intersection(nations))[0]
    return 'Not Found'


def main():
    print(drinks_water(), 'drinks water.')
   # print(owns_zebra(), 'owns zebra.')
    
    
if __name__ == '__main__':
    main()
