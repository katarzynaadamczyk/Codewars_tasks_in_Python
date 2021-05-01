import math

# non-tested functions
def an(n):
    # returns first n terms of the series a(n)
    out = [7]
    for i in range(2, n + 1):
        out.append(out[-1] + math.gcd(i, out[-1]))
    return out

def gn(n):
    # returns first n terms of the series g(n) + 1 for n = 1
    an_n = an(n)
    gn_n = [1]
    for i in range(1, len(an_n)):
        gn_n.append(an_n[i] - an_n[i - 1])
    return gn_n

def count_not_ones(n):
    # returns the number of not-1's in the series g(n)
    return len([i for i in gn(n) if i != 1])

def p(n):
    # returns first n primes exluding 1's in same order they are in gn(n)
    
    m = n # minimum
    maxi = n * 2 ** 1000 # maximum
    n2 = (m + maxi) // 2 # average
    count = count_not_ones(n2)
    while count != n:
        if count < n:
            m = n2
            n2 = (maxi + n2) // 2
        else:
            maxi = n2
            n2 = (n2 + m) // 2
        count = count_not_ones(n2)
    return [i for i in gn(n2) if i != 1]

def an_over(n):
    # returns an array of size n of the a(i) / i for every g(i) != 1
    pass




# tested functions

def count_ones(n):
    # returns the number of 1's in the series g(n)
    return len([i for i in gn(n) if i == 1])

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
    print(f'count_not_ones(100) = {count_not_ones(100)}')
    print(f'count_not_ones(200) = {count_not_ones(200)}')
    print('p(1)')
    print(p(1))
    print('p(10)')
    print(p(10))
   # print('p(100)')
  #  print(p(100))



if __name__ == '__main__':
    main()