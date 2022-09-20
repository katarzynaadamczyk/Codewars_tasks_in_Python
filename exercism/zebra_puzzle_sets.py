''' zebra puzzle solved on sets '''

from copy import deepcopy
from functools import reduce

colors = {'red', 'green', 'blue', 'ivory', 'yellow'}
nations = {'English', 'Spaniard', 'Japanese', 'Norwegian', 'Ukrainian'}
animals = {'dog', 'zebra', 'snails', 'horse', 'fox'}
beverages = {'coffee', 'water', 'tea', 'milk', 'orange juice'}
cigarettes = {'Kools', 'Old Gold', 'Chesterfields', 'Lucky Strike', 'Parliaments'}

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
                if index > 0 and (house & animals)== set() and (solution[index - 1] & cigarettes) == set():
                    new_solution = deepcopy(solution)
                    new_solution[index].add(animal)
                    new_solution[index - 1].add(cigar)
                    new_solutions.append(new_solution)
                if index < len(solution) - 1 and (house & animals) == set() and (solution[index + 1] & cigarettes) == set():
                    new_solution = deepcopy(solution)
                    new_solution[index].add(animal)
                    new_solution[index + 1].add(cigar)
                    new_solutions.append(new_solution)
        all_solutions = new_solutions
        new_solutions = []
    return all_solutions


def solution_union(solution):
    return reduce(lambda x, y: x.union(y), solution)


def add_trait(solution, trait1, trait2, index_type):
    for house_index, house in enumerate(solution):
        if trait1 in house and (house & all[index_type]) == set():
            new_solution = deepcopy(solution)
            new_solution[house_index].add(trait2)
            return new_solution
    return solution


def print_all_solutions(all_solutions):
    for index, solution in enumerate(all_solutions):
        print(index, ":")
        for house_number, values in enumerate(solution):
            print(house_number, ":", values)
        print()


def easy_hints_adder(all_solutions):
    new_solutions, index1_type, index2_type = [], 0, 0
    for trait1, trait2 in easy_hints:
        for trait_index, type in enumerate(all):
            if trait1 in type:
                index1_type = trait_index
            if trait2 in type:
                index2_type = trait_index
        for solution in all_solutions:
            solution_set = solution_union(solution)
            if ({trait1, trait2} & solution_set) == set():
                for house_index, house in enumerate(solution):
                    if (house & all[index1_type]) == (house & all[index2_type]):
                        new_solution = deepcopy(solution)
                        new_solution[house_index].add(trait1)
                        new_solution[house_index].add(trait2)
                        new_solutions.append(new_solution)
            elif trait1 in solution_set and trait2 not in solution_set:
                new_solution = add_trait(solution, trait1, trait2, index2_type)
                if solution_union(new_solution) != solution_set:
                    new_solutions.append(new_solution)
            elif trait2 in solution_set and trait1 not in solution_set:
                new_solution = add_trait(solution, trait2, trait1, index1_type)
                if solution_union(new_solution) != solution_set:
                    new_solutions.append(new_solution)
        all_solutions = new_solutions
        new_solutions = []
    return all_solutions


def solve():
    solution = [set(), set(), set(), set(), set()]
    solution[0].add('Norwegian')
    solution[1].add('blue')
    solution[2].add('milk')
    all_solutions = [solution]
    
    all_solutions = green_ivory_hint(all_solutions)
    all_solutions = animal_cigarette_hint(all_solutions)
    all_solutions = easy_hints_adder(all_solutions)
    
    solution = all_solutions[0]
    
    for house_index, house in enumerate(solution):
        if house & beverages == set():
            solution[house_index].add('water')
        if house & animals == set():
            solution[house_index].add('zebra')
    
    
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
    print(owns_zebra(), 'owns zebra.')
    
    
if __name__ == '__main__':
    main()
