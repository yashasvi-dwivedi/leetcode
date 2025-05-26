class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # Initialize the node's value and next pointer


class Solution(object):
    def reverseBetween(self, head, left, right):
        # If the list is empty or left == right, no need to reverse
        if not head or left == right:
            return head

        dummy = ListNode(0)  # Dummy node to simplify edge cases
        dummy.next = head
        prev = dummy

        # Move prev to the node just before the 'left' position
        for _ in range(left - 1):
            prev = prev.next

        current = prev.next  # The first node to be reversed
        # Reverse the sublist from left to right
        for _ in range(right - left):
            next_node = current.next  # Node to be moved
            current.next = next_node.next  # Remove next_node from its current position
            next_node.next = prev.next  # Insert next_node after prev
            prev.next = next_node  # Update prev to point to next_node

        return dummy.next  # Return the new head (could be different if left == 1)


def list_to_linkedlist(lst):
    # Helper function to convert a Python list to a linked list
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linkedlist(head):
    # Helper function to print the linked list as a Python list
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
    print_linkedlist(result)  # Output: [5]
