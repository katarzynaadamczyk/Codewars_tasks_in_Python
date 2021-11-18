import time
import numpy as np
from typing import List

def measuretime(func):
    def wrapper(*args, **kwargs):
        starttime = time.perf_counter_ns()
        ret = func(*args, **kwargs)
        endtime = time.perf_counter_ns()
        print(f'Time needed: {endtime - starttime} ns')
        return ret
    return wrapper

def measuretime2(func, n):
    starttime = time.perf_counter_ns()
    ret = func(n)
    endtime = time.perf_counter_ns()
    print(f'Time needed: {endtime - starttime} ns')
    return ret

# first solution - too long
@measuretime
def fib(n):
    lst = []
    lst.append(0)
    lst.append(1)
    if n >= 0:
        for i in range(2, n + 1):
            lst.append(lst[i - 1] + lst[i - 2])
        return lst[n]
    for i in range(n, 0):
        lst.insert(0, lst[1] - lst[0])
    return lst[0]

# second solution - way too long
def fib_v2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib_v2(n - 1) + fib_v2(n - 2)
    return fib_v2(n + 2) - fib_v2(n + 1)

# third solution - using numpy
@measuretime
def fib_v3(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n - 2 > 2:
        def fib_log(a: int, b: int, c: int, d: int, n: int) -> List[int]:
            tab1 = np.array([[a, b], [c, d]])
            ret = np.array([[1, 0], [0, 1]])
            while n > 0:
                if n % 2 == 0:
                    ret = np.matmul(ret, tab1, tab1)
                    n = n // 2
                else:
                    ret = np.matmul(tab1, ret)
                    n -= 1
            return ret
        tab = fib_log(0, 1, 1, 1, n - 2)
        print(tab)
        tab = np.matmul(tab, np.array([[0], [1]]))
        return sum(tab)
        
    return -1

def main():
    for n in range(-10, 31, 5):
        result = fib(n)
        print(f'First sol for {n} is {result}')
        result = measuretime2(fib_v2, n)
        print(f'Second sol for {n} is {result}')
    result = fib_v3(10)
    print(f'Third sol for 10 is {result[0]}')
    

if __name__ == '__main__':
    main()