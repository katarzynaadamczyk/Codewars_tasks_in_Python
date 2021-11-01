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
    def add_node(num, next=None):  
        node = ListNode(num, next=next)
        return node

    @staticmethod
    def create_node_list(nums=[]): 
        next = None
        for num in nums:
            next = Solution.add_node(num, next)
        return next
    
    @staticmethod
    def print_linked_list(node): 
        print('[', end='')
        while node:
            print(node.val, end='')
            node = node.next
            if node:
                print(', ', end='')
        print(']')

    @staticmethod
    def print_reversed_linked_list(node): 
        lst = []
        while node:
            lst.insert(0, node.val)
            node = node.next
        print(lst)

    @staticmethod
    def get_number_from_node(node): 
        num = 0
        i = 0
        while node:
            num += node.val * 10 ** i
            i += 1
            node = node.next
        return num


    @staticmethod # TO CHANGE - I GET ONLY FIRST LIST NODE!!!
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return [0]
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        prev = 0
        first_node = None
        last_node = None


        while l1 is not None and l2 is not None:
            if l1 is None:
                add = (prev + l2.val) % 10
                prev = (prev + l2.val) // 10
                l2 = l2.next
            elif l2 is None:
                add = (prev + l1.val) % 10
                prev = (prev + l1.val) // 10
                l1 = l1.next
            else:
                add = (prev + l1.val + l2.val) % 10
                prev = (prev + l1.val + l2.val) // 10
                l1 = l1.next
                l2 = l2.next
            if first_node is None:
                first_node = Solution.add_node(add, next=None)
                last_node = first_node
            else:
                tmp = Solution.add_node(add, next=None)
                last_node.next = tmp
                last_node = tmp
        if prev > 0:
            tmp = Solution.add_node(prev, next=None)
            last_node.next = tmp
        return first_node


    @staticmethod # TO CHANGE - I GET ONLY ADDRESS OF THE FIRST ELEMENT OF LINKED LIST
    def addTwoNumbers2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = Solution.get_number_from_list(l1)
        num2 = Solution.get_number_from_list(l2)
        return Solution.create_node_list([int(x) for x in str(num1+num2)])






def main():
    # first list
    lst = Solution.create_node_list([3, 4, 2])
    Solution.print_linked_list(lst)
    Solution.print_reversed_linked_list(lst)
    print(Solution.get_number_from_node(lst))

    # second list
    sec = Solution.create_node_list([4, 6, 5])
    Solution.print_linked_list(sec)
    Solution.print_reversed_linked_list(sec)
    print(Solution.get_number_from_node(sec))

    # solution
    print(Solution.get_number_from_node(Solution.addTwoNumbers(lst, sec)))
    #print(Solution.get_number_from_list(Solution.addTwoNumbers2(lst, sec)))
    print(Solution.get_number_from_node(lst) + Solution.get_number_from_node(sec))



    pass


if __name__ == '__main__':
    main()