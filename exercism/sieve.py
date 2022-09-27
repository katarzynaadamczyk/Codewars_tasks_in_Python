''' sieve exercise '''

def primes(limit):
    non_primes = set()
    for number in range(2, limit + 1):
        if number not in non_primes:
            new_number = number + number
            while new_number <= limit:
                non_primes.add(new_number)
                new_number += number
    return [number for number in range(2, limit + 1) if number not in non_primes]

def main():
    print(primes(10))

if __name__ == '__main__':
    main()
    