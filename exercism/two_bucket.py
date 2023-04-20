''' exercise two bucket '''

from math import gcd

class Bucket:
    def __init__(self, name, capacity, val=0):
        self.capacity = capacity
        self.name = name
        self.act_val = val

def measure(bucket_one, bucket_two, goal, start_bucket):    
    if not (goal <= bucket_one or goal <= bucket_two):
        raise ValueError('goal bigger than buckets')    
    if goal % gcd(bucket_one, bucket_two) != 0:
        raise ValueError('cannot reach target')
    return (0, "one", 0)

def main():
    print(measure(3, 5, 1, "one"), 'should equal:', (4, "one", 5))
    print(measure(1, 3, 3, "two"), 'should equal:', (1, "two", 0))

if __name__ == '__main__':
    main()
    