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

    if count_of_evens >= len(evens) - 1:
        return count_of_evens // 2
    if count_of_evens < 2:
        return count_of_evens
    
    i, count_act, result = 0, 0, 0

    while evens[i] == 1:
        i -= 1

    for j in range(i, len(evens) + i):
        if evens[j] == 1:
            count_act += 1
        else:
            result += (count_act + 1) // 2
            count_act = 0

    return result + (count_act + 1) // 2
    

def main():
    print(f'Solution for [4,2,5,8,7,3,7] is {solution([4,2,5,8,7,3,7])} (it should equal 2)')
    print(f'Solution for [14,21,16,35,22] is {solution([14,21,16,35,22])} (it should equal 1)')
    print(f'Solution for [5,5,5,5,5,5] is {solution([5,5,5,5,5,5])} (it should equal 3)')
    print(f'Solution for [5,5,2,7,3,1,3,4,10,2] is {solution([5,5,2,7,3,1,3,4,10,2])} (it should equal 4)')


if __name__ == '__main__':
    main()