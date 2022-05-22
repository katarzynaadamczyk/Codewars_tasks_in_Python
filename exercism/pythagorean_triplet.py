''' exercise pythagorean triplet '''

from math import gcd

from matplotlib import mlab

# solution 1 - two for loops

def get_numbers(number):
    for a in range(1, number // 3 + 1):
        b = a + 1
        c = number - a - b
        while c > b:
            yield a, b, c
            b += 1
            c -= 1

# problem with large numbers
def triplets_with_sum_v1(number):
    result = []
    for a, b, c in get_numbers(number):
        if (a ** 2 + b ** 2) == c ** 2:
            result.append([a, b, c])
    return result

# second solution - one for loop, b and c counted with appropriate formulas
# a ** 2 + b ** 2 = c  ** 2
# a + b + c = number -> c = number - a - b
# a ** 2 + b ** 2 = (number - a - b) ** 2
def triplets_with_sum_v2(number):
    result = set()
    for a in range(1, number):
        b = (number ** 2 - 2 * number * a) // (2 * number - 2 * a)
        c = number - a - b
        if (a ** 2 + b ** 2 == c ** 2) and b > 0 and c > 0:
            result.add(tuple(sorted([a, b, c])))
    return sorted([list(x) for x in result])

if __name__ == '__main__':
   # print(triplets_with_sum_v1(108))
    print(triplets_with_sum_v2(30000))