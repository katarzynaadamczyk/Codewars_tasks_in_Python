''' sieve exercise '''

def primes(limit):
    lst_of_primes, non_primes = list(range(2, limit + 1)), set()
    for number in lst_of_primes:
        if number not in non_primes:
            new_number = number + number
            while new_number <= limit:
                non_primes.add(new_number)
                new_number += number
    return [number for number in lst_of_primes if number not in non_primes]

def main():
    print(primes(10))

if __name__ == '__main__':
    main()
    