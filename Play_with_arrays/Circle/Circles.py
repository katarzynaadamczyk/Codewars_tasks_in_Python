from typing import List

def solution(nums: List[int]) -> int:
    result1 = 0
    result2 = 0
    for i in range(-1, len(nums) - 1):
        if (nums[i] + nums[i+1]) % 2 == 0:
            if i % 2 == 0:
                result1 += 1
            else: 
                result2 += 1
    return result1 if result1 > result2 else result2


def main():
    print(f'Solution for [4,2,5,8,7,3,7] is {solution([4,2,5,8,7,3,7])}')
    print(f'Solution for [14,21,16,35,22] is {solution([14,21,16,35,22])}')
    print(f'Solution for [5,5,5,5,5,5] is {solution([5,5,5,5,5,5])}')
    


if __name__ == '__main__':
    main()