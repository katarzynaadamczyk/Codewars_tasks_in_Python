''' my solution to task: https://www.codewars.com/kata/62013b174c72240016600e60/ '''

from collections import Counter

correct = 'g'
wrong_place = 'y'
not_in_word = 'b'

def resolver(guess, solution):    
    # getting counters for solution and guess
    solution_counter = Counter(solution)
    guess_counter = Counter()
    
    # comparing and adding correct colors
    result = [not_in_word for _ in range(5)]
    # adding corrects
    for index, char in enumerate(guess):
        if solution[index] == char:
            result[index] = correct
            guess_counter[char] += 1
    
    # adding wrong places
    for index, char in enumerate(guess):
        if result[index] == not_in_word:
            if guess_counter[char] < solution_counter[char]:
                result[index] = wrong_place
                guess_counter[char] += 1
    
    return ''.join(result)

def main():
    print(resolver('blows', 'world'), '? byyyb', "(guess: 'blows', answer: 'world' => 'byyyb')")

if __name__ == '__main__':
    main()
    
    