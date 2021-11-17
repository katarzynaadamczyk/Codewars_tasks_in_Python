import time

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

# third solution - hope to be good
def fib_v3(n):
    pass


def main():
    for n in range(-10, 31, 5):
        result = fib(n)
        print(f'First sol for {n} is {result}')
        result = measuretime2(fib_v2, n)
        print(f'Second sol for {n} is {result}')
    

if __name__ == '__main__':
    main()