''' exercise factors '''

from math import sqrt

def get_prime_factor(range_value):
    yield 2
    yield 3
    for index in range(1, int(sqrt(range_value)) + 1):
        yield 6 * index - 1
        yield 6 * index + 1

def factors(value):
    factors = []
    for factor in get_prime_factor(value):
        while value % factor == 0:
            factors.append(factor)
            value //= factor
        if value == 1:
            break
    return factors

if __name__ == '__main__':
    print(factors(10))
    print(factors(100))
    print(factors(300))