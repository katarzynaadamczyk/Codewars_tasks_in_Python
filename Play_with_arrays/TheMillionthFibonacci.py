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

# third solution - using numpy - still a long one and not precise enough 
@measuretime
def fib_v3(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    def fib_log(a: int, b: int, c: int, d: int, n: int) -> List[int]:        
        
        lst = []
        
        while n > 0:
            if n % 2:
                lst.insert(0, 1)
                n -= 1
            while n % 2 == 0 and n > 0:
                lst.insert(0, 2)
                if n == 2:
                    n = 0
                else:
                    n = n // 2
        
        ret = np.array([[1, 0], [0, 1]], dtype=np.uint64) if lst[0] == 1 else np.array([[a, b], [c, d]], dtype=np.uint64)
        tab1 = np.array([[a, b], [c, d]], dtype=np.uint64)
        
        for i in lst:
            if i == 1:
                ret = np.matmul(ret, tab1)
            else:
                ret = np.matmul(ret, ret)

        return np.matmul(ret, np.array([[0], [1]]))
    
    if n > 2:    
        tab = fib_log(0, 1, 1, 1, n)
        return int(tab[0][0])
    else:
        tab = fib_log(0, 1, 1, 1, -1 * n)
        return int(tab[0][0]) if n % 2 else int(tab[0][0]) * (-1)
    
# 4th solution - best solution - working well, fast and precise 
@measuretime
def fib_v4(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    def fib_log(a: int, b: int, c: int, d: int, n: int) -> int:        
        
        lst = []
        
        while n > 0:
            if n % 2:
                lst.insert(0, 1)
                n -= 1
            while n % 2 == 0 and n > 0:
                lst.insert(0, 2)
                if n == 2:
                    n = 0
                else:
                    n = n // 2
        
        a1 = 1 if lst[0] == 1 else a
        b1 = 0 if lst[0] == 1 else b
        c1 = 0 if lst[0] == 1 else c
        d1 = 1 if lst[0] == 1 else d
        a2, b2, c2, d2 = 0, 0, 0, 0
        
        for i in lst:
            if i == 1:
                a2 = a1 * a + b1 * c
                b2 = a1 * b + b1 * d
                c2 = c1 * a + d1 * c
                d2 = c1 * b + d1 * d
                a1, b1, c1, d1 = a2, b2, c2, d2
            else:
                a2 = a1 * a1 + b1 * c1
                b2 = a1 * b1 + b1 * d1
                c2 = c1 * a1 + d1 * c1
                d2 = c1 * b1 + d1 * d1
                a1, b1, c1, d1 = a2, b2, c2, d2

        return b1
    
    if n > 2:    
        return fib_log(0, 1, 1, 1, n)
    else:
        return fib_log(0, 1, 1, 1, -1 * n) * (1 if n % 2 else (-1))
    
    


def main():
    for n in range(20, 26):
        result1 = fib(n)
        result2 = measuretime2(fib_v2, n)
        result3 = fib_v3(n)
        result4 = fib_v4(n)
        print(f'Solutions for n = {n}: \t{result1}\t{result2}\t{result3}\t{result4}')     
        
        
    for n in range(-25, -19):
        result1 = fib(n)
        result2 = measuretime2(fib_v2, n)
        result3 = fib_v3(n)
        result4 = fib_v4(n)
        print(f'Solutions for n = {n}: \t{result1}\t{result2}\t{result3}\t{result4}') 

if __name__ == '__main__':
    main()