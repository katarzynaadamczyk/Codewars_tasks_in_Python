# first solution - too long

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

def fib_v2(n):
    pass


def main():
    pass
    

if __name__ == '__main__':
    main()