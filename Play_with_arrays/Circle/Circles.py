from typing import List

def solution(nums: List[int]) -> int:
    



    #evens = []
    #for i in range(-1, len(nums) - 1):
    #    if (nums[i] + nums[i+1]) % 2 == 0:
    #        evens.append(1)
    #    else:
    #        evens.append(0)
    #print(evens)
   
    count_max = 0
    for i in range(-1, len(nums) - 1):
        count_act = 0
        i2 = i
        first = False
        while True:
            if (nums[i2] + nums[i2+1]) % 2 == 0:
                count_act += 1
                i2 += 2
                if i2 == len(nums - 1):
                    pass
                # problem z zakrecaniem
            else:
                i2 += 1
                
            if first and (i2 == i or i2 == i + 1):
                break
            first = True
        
        if count_act > count_max:
            count_max = count_act
        
    return count_max 
    
    

def main():
    print(f'Solution for [4,2,5,8,7,3,7] is {solution([4,2,5,8,7,3,7])} (it should equal 2)')
    #print(f'Solution for [14,21,16,35,22] is {solution([14,21,16,35,22])} (it should equal 1)')
    #print(f'Solution for [5,5,5,5,5,5] is {solution([5,5,5,5,5,5])} (it should equal 3)')
    #print(f'Solution for [5,5,2,7,3,1,3,4,10,2] is {solution([5,5,2,7,3,1,3,4,10,2])} (it should equal 4)')


if __name__ == '__main__':
    main()