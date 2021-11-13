from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def removeHead(head: ListNode):
            head2 = head.next
            del head
            return head2

        while head.val == val:
            head = removeHead(head)
        
        pom = head
        while pom:
            if pom.next is not None and pom.next.val == val:
                pom.next = removeHead(pom.next)
            else:
                pom = pom.next
        
        return head


def create_linked_list(arr: Optional[List[int]]) -> Optional[ListNode]:
    if not arr:
        return None
    head = None
    for i in reversed(arr):
        head = ListNode(i, head)
    return head

def print_linked_list(head: Optional[ListNode]):
    print('[', end='')
    while head and head.next:
        print(str(head.val) + ', ', end='')
        head = head.next
    print(str(head.val) + ']')

def main():
    head = create_linked_list([1, 2, 5, 6, 4, 7, 8])
    print(head)
    print_linked_list(head)
    head2 = Solution.removeElements(head, 6)
    print(head)
    print(head2)
    print_linked_list(head)
    print_linked_list(head2)
    

if __name__ == '__main__':
    main()
    