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

# third solution - using numpy negative not working well, 
@measuretime
def fib_v3(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    def fib_log(a: int, b: int, c: int, d: int, n: int) -> List[int]:
        ret = np.array([[1, 0], [0, 1]], dtype=np.uint64)
        print(n)
        while n > 0:
            tab1 = np.array([[a, b], [c, d]], dtype=np.uint64)
            if n % 2:
                ret = np.matmul(ret, tab1)
                n -= 1
            print(n)
            print(ret)
            while n % 2 == 0 and n > 0:
                tab1 = np.matmul(tab1, tab1)
                if n == 2:
                    n = 0
                else:
                    n = n // 2
            ret = np.matmul(ret, tab1)
            print(n)
            print(ret)
            
            
        
        print(f'ret:')
        print(ret)
        return np.matmul(ret, np.array([[0], [1]]))
    
    if n > 2:    
        tab = fib_log(0, 1, 1, 1, n)
        return np.sum(tab)
    else:
        tab = fib_log(0, 1, 1, 1, (-1 * n) - 2)
        return int(np.sum(tab)) if n % 2 else int(-1 * np.sum(tab))
    
# 4th solution
@measuretime
def fib_v4(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    def fib_log(a: int, b: int, c: int, d: int, n: int) -> int:
        tab1 = np.array([[a, b], [c, d]])
        ret = np.array([[a, b], [c, d]]) #if n % 2 == 0 else np.array([[1, 0], [0, 1]])
        m = 0
        while n > 1:
            print(f'Steps count: {m}, n = {n}, ret:')
            print(ret)
            m += 1
            if n % 2 == 0:
                ret = np.matmul(ret, ret)
                n = n // 2
            else:
                ret = np.matmul(tab1, ret)
                n -= 1
        print(f'm = {m}, n= {n}, ret:')
        print(ret)
        return np.matmul(ret, np.array([[0], [1]]))
    
    if n > 2:    
        tab = fib_log(0, 1, 1, 1, n - 2)
        return np.sum(tab)
    else:
        tab = fib_log(0, 1, 1, 1, (-1 * n) - 2)
        return int(np.sum(tab)) if n % 2 else int(-1 * np.sum(tab))

def main():
    for n in range(5,11):
        result = fib(n)
        print(f'First sol for {n} is {result}')
        result = measuretime2(fib_v2, n)
        print(f'Second sol for {n} is {result}')
        result = fib_v3(n)
        print(f'Third sol for {n} is {result}')
    #result = fib_v3(1000)
    #print(f'Third sol for 1000 is {result}')
    #print(f'Third sol for 1000 is 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875')
    
    

if __name__ == '__main__':
    main()