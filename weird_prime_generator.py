import math

# non-tested functions
def an(n):
    # returns first n terms of the series a(n)
    if n == 1:
        return [7]
    an_1 = an(n - 1)
    an_1.append(an_1[-1] + math.gcd(n, an_1[-1]))
    return an_1

def gn(n):
    # returns first n terms of the series g(n) + 1 for n = 1
    an_n = an(n)
    gn_n = [1]
    for i in range(1, len(an_n)):
        gn_n.append(an_n[i] - an_n[i - 1])
    return gn_n

def p(n):
    # returns first n primes exluding 1's in same order they are in gn(n)
    pass

def an_over(n):
    # returns an array of size n of the a(i) / i for every g(i) != 1
    pass




# tested functions

def count_ones(n):
    # returns the number of 1's in the series g(n)
    # your code
    pass

def max_pn(n):
    # returns the biggest prime number of p(n)
    # your code
    pass

def an_over_average(n):
    # returns an integer average of the an_over(n)
    # your code
    pass

def main():
    out = count_ones(1)
    print(out) 
    print('Should be 1')
    out = count_ones(10)
    print(out) 
    print('Should be 8')
    out = count_ones(100)
    print(out) 
    print('Should be 90')
    out = max_pn(1)
    print(out) 
    print('Should be 5')
    out = max_pn(5)
    print(out) 
    print('Should be 47')
    out = an_over_average(1)
    print(out) 
    print('Should be 3')
    print('an(25)')
    print(an(25))
    print('gn(25)')
    print(gn(25))

if __name__ == '__main__':
    main()