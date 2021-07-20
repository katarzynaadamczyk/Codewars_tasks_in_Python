from typing import List

def solution(nums: List[int]) -> int:
    evens = []
    for i in range(-1, len(nums) - 1):
        if (nums[i] + nums[i+1]) % 2 == 0:
            evens.append(1)
        else:
            evens.append(0)
    # teraz jeszcze przejsc i sprawdzic jak to zrobic
    while True:

        pass    
    


def main():
    print(f'Solution for [4,2,5,8,7,3,7] is {solution([4,2,5,8,7,3,7])}')
    print(f'Solution for [14,21,16,35,22] is {solution([14,21,16,35,22])}')
    print(f'Solution for [5,5,5,5,5,5] is {solution([5,5,5,5,5,5])}')
    print(f'Solution for [5,5,2,7,3,1,3,4,10,2] is {solution([5,5,2,7,3,1,3,4,10,2])} (it should equal 4')


if __name__ == '__main__':
    main()