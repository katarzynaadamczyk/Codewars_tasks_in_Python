from typing import List

class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        if nums1 is None and nums2 is None:
            return None
        if nums1 is None:
            lst = nums2
        elif nums2 is None:
            lst = nums1
        else:
            lst = []
            j = 0
            for i in nums1:
                while j < len(nums2) and i >= nums2[j]:
                    lst.append(nums2[j])
                    j += 1
                lst.append(i)
            for i in range(j, len(nums2)):
                lst.append(nums2[i])
        print(lst)
        return lst[len(lst) // 2] if len(lst) % 2 == 1 else (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
                
                

def main():
    print('First Solution:')
    print(f'For: [1, 2, 3] and [4, 5, 6] solution is {Solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6])} (should be 3,5)')
    print(f'For: [1, 3] and [2] solution is {Solution.findMedianSortedArrays([1, 3], [2])} (should be 2)')
    
    

if __name__ == '__main__':
    main()