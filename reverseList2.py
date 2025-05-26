class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next


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
    result = s.reverseBetween(head, 2, 4)
    print_linkedlist(result)  # Output: [1, 4, 3, 2, 5]

    head = list_to_linkedlist([5])
    result = s.reverseBetween(head, 1, 1)
    print_linkedlist(result)
