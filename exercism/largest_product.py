''' exercise largest series product '''

import re
from functools import reduce
from math import prod

def largest_product_v1(series, size):
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if len(re.findall(r'\d', series)) != len(series):
        raise ValueError("digits input must only contain digits")
    if size == 0:
        return 1
    return max([prod([int(char) for char in series[i:i+size]]) for i in range(len(series) + 1 - size)])


def largest_product_v2(series, size):
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if len(re.findall(r'\d', series)) != len(series):
        raise ValueError("digits input must only contain digits")
    if size == 0:
        return 1
    return max([reduce(lambda x,y: x*y, [int(char) for char in series[i:i+size]]) for i in range(len(series) + 1 - size)])
