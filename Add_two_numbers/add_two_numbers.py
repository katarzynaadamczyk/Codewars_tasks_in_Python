from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print_node(self, end='\n'):
        print(self.val, end=end)


class Solution:
    
    @staticmethod
    def add_node(num, lst=[]): # add this function to solution class ?
        if len(lst):
            node = ListNode(num, next=lst[0])
        else:
            node = ListNode(num, next=None)
        lst.insert(0, node)
        return lst

    @staticmethod
    def create_node_list(nums=[]):
        lst = []
        for num in nums:
            Solution.add_node(num, lst)
        return lst
    
    @staticmethod
    def print_linked_list(lst):
        print('[', end='')
        if len(lst):
            for i in range(len(lst) - 1):
                lst[i].print_node(end=', ')
            lst[-1].print_node(end='')
        print(']')

    @staticmethod
    def print_reversed_linked_list(lst):
        print('[', end='')
        if len(lst):
            for i in range(len(lst) - 1):
                lst[len(lst) - 1 - i].print_node(end=', ')
            lst[0].print_node(end='')
        print(']')

    @staticmethod
    def get_number_from_list(lst):
        num = 0
        for i in range(len(lst)):
            num += lst[i].val * 10 ** i
        return num


    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return [0]
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        prev = 0
        lst = []
        it1 = l1[0]
        it2 = l2[0]

        while it1 is not None and it2 is not None:
            if it1 is None:
                add = (prev + it2.val) % 10
                prev = (prev + it2.val) // 10
                it2 = it2.next
            elif it2 is None:
                add = (prev + it1.val) % 10
                prev = (prev + it1.val) // 10
                it1 = it1.next
            else:
                add = (prev + it1.val + it2.val) % 10
                prev = (prev + it1.val + it2.val) // 10
                it1 = it1.next
                it2 = it2.next
            Solution.add_node(add, lst)
        if prev > 0:
            Solution.add_node(prev, lst)
        return lst


    @staticmethod
    def addTwoNumbers2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = Solution.get_number_from_list(l1)
        num2 = Solution.get_number_from_list(l2)
        return Solution.create_node_list([int(x) for x in str(num1+num2)])






def main():
    # first list
    lst = Solution.create_node_list([3, 4, 2])
    Solution.print_linked_list(lst)
    Solution.print_reversed_linked_list(lst)

    # second list
    sec = Solution.create_node_list([4, 6, 5])
    Solution.print_linked_list(sec)
    Solution.print_reversed_linked_list(sec)

    # solution
    print(Solution.get_number_from_list(Solution.addTwoNumbers(lst, sec)))
    print(Solution.get_number_from_list(Solution.addTwoNumbers2(lst, sec)))
    print(Solution.get_number_from_list(lst) + Solution.get_number_from_list(sec))



    pass


if __name__ == '__main__':
    main()