''' exercise perfect numbers '''

from math import sqrt

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = set()
    if number > 1:
        factors.add(1)
    for num in range(2, int(sqrt(number)) + 1):
        if number % num == 0:
            factors.add(num)
            factors.add(number // num)
            number //= num
    sum_of_factors = sum(factors)
    if sum_of_factors == number:
        return 'perfect'
    elif sum_of_factors < number:
        return 'deficient'
    else:
        return 'abundant'

if __name__ == '__main__':
    print(classify(1))