class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linkedlist(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


# Test Case
if __name__ == "__main__":
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    s = Solution()
    result = s.reverseList(head)
    print_linkedlist(result)
