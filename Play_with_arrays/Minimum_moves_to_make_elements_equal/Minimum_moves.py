class Solution:
    # pierwsze rozwiazanie niedokonczone
    def minMoves2(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums[0] == sorted_nums[-1]:
            return 0
        
        num = sorted_nums[0]
        
        nums_count = {num: 1}

        for i in range(1, len(nums)):
            if num == sorted_nums[i]:
                nums_count[num] += 1
            else:
                num = sorted_nums[i]
                nums_count.setdefault(num, 1)
        
        # mamy posortowane numery w sorted_nums 
        # mamy slownik zawierajacy wszystkie numery i ich ilosc

        pass

    # drugie rozwiazanie not working yet
    def minMoves3(self, nums: List[int]) -> int:
        nums_count = {}
        for i in nums:
            nums_count.setdefault(i, 0)
            nums_count[i] += 1

        nums_sum = sum(nums)
        avg = nums_sum // len(nums)
        result = 0

        for key in nums_sum.keys():
            result += abs(avg - key) * nums_count[key]

        return result           
