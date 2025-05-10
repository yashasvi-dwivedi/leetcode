class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None

        count = 0
        current_node = head
        while current_node is not None:
            current_node = current_node.next
            count += 1

        mid = count // 2

        current_node = head
        for _ in range(mid - 1):
            current_node = current_node.next

        current_node.next = current_node.next.next

        return head


# Example usage:
# Assuming ListNode is defined as follows:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Creating a linked list for demonstration
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# Deleting the middle node
solution = Solution()
new_head = solution.deleteMiddle(head)


# Printing the modified linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


print_list(new_head)
# Output: 1 -> 2 -> 4 -> 5 -> None
