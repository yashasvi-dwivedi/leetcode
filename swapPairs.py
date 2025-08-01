from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            npn = cur.next.next
            second = cur.next

            # Swap
            second.next = cur
            cur.next = npn
            prev.next = second

            # Move pointers forward
            prev = cur
            cur = npn
        return dummy.next


# Test cases
if __name__ == "__main__":

    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    # Helper to create linked list from Python list
    def list_to_linkedlist(lst):
        dummy = ListNode()
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    # Create a linked list: 1 -> 2 -> 3 -> 4
    head = list_to_linkedlist([1, 2, 3, 4])
    sol = Solution()
    swapped_head = sol.swapPairs(head)
    print_list(swapped_head)  # Output: 2 -> 1 -> 4 -> 3 -> None
