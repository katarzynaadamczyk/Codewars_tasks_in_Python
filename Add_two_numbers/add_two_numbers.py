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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return [0]
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        prev = 0
        
        # TODO
        pass

def add_node(num, lst=[]):
    if len(lst):
        node = ListNode(num, next=lst[0])
    else:
        node = ListNode(num, next=None)
    lst.insert(0, node)
    return lst

def print_linked_list(lst):
    print('[', end='')
    if len(lst):
        for i in range(len(lst) - 1):
            lst[i].print_node(end=', ')
        lst[-1].print_node(end='')
    print(']')

def print_reversed_linked_list(lst):
    print('[', end='')
    if len(lst):
        for i in range(len(lst) - 1):
            lst[len(lst) - 1 - i].print_node(end=', ')
        lst[0].print_node(end='')
    print(']')

def main():
    # first list
    lst = []
    add_node(3, lst)
    add_node(4, lst)
    add_node(2, lst)
    print_linked_list(lst)
    print_reversed_linked_list(lst)

    # second list
    sec = []
    add_node(4, sec)
    add_node(6, sec)
    add_node(5, sec)
    print_linked_list(sec)
    print_reversed_linked_list(sec)

    # solution


    pass


if __name__ == '__main__':
    main()