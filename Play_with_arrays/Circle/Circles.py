from typing import List

def solution(nums: List[int]) -> int:
    
    # create an array filled with 1 if there is a corresponding even sum in the circle
    # and filled with 0 otherwise
    # count_of_evens - stores the count of 1's in the array

    evens, count_of_evens = [], 0
    for i in range(-1, len(nums) - 1):
        if (nums[i] + nums[i+1]) % 2 == 0:
            evens.append(1)
            count_of_evens += 1
        else:
            evens.append(0)

    if count_of_evens == len(evens):
        return len(evens) // 2
    if count_of_evens < 2:
        return count_of_evens
    
    count_neighbours_1 = 0
    count_neighbours_2 = 0

    for i in range(len(evens)):
        if evens[i] == 1 and evens[i - 1] == 1:
            count_neighbours_1 += 1
            if evens[i-2] == 1:
                count_neighbours_2 += 1    

    return count_of_evens - count_neighbours_1 + count_neighbours_2


def solution_v2(nums: List[int]) -> int:

    if len(nums) < 2:
        return 0
    if len(nums) == 2:
        if nums[0] + nums[1] % 2 == 0:
            return 1
        return 0
    

    count_of_evens = 0
    count_neighbours_1 = 0
    count_neighbours_2 = 0

    for i in range(-2, len(nums) - 2):
        if (nums[i] + nums[i+1]) % 2 == 0:
            count_of_evens += 1
            if (nums[i-1] + nums[i]) % 2 == 0:
                count_neighbours_1 += 1
                if (nums[i+1] + nums[i+2]) % 2 == 0:
                    count_neighbours_2 += 1

    return count_of_evens - count_neighbours_1 + count_neighbours_2
    
    

def main():
    print('Solution v1')
    print(f'Solution for [4,2,5,8,7,3,7] is {solution([4,2,5,8,7,3,7])} (it should equal 2)')
    print(f'Solution for [14,21,16,35,22] is {solution([14,21,16,35,22])} (it should equal 1)')
    print(f'Solution for [5,5,5,5,5,5] is {solution([5,5,5,5,5,5])} (it should equal 3)')
    print(f'Solution for [5,5,2,7,3,1,3,4,10,2] is {solution([5,5,2,7,3,1,3,4,10,2])} (it should equal 4)')
    print('Solution v2')
    print(f'Solution for [4,2,5,8,7,3,7] is {solution([4,2,5,8,7,3,7])} (it should equal 2)')
    print(f'Solution for [14,21,16,35,22] is {solution([14,21,16,35,22])} (it should equal 1)')
    print(f'Solution for [5,5,5,5,5,5] is {solution([5,5,5,5,5,5])} (it should equal 3)')
    print(f'Solution for [5,5,2,7,3,1,3,4,10,2] is {solution([5,5,2,7,3,1,3,4,10,2])} (it should equal 4)')


if __name__ == '__main__':
    main()