class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head):
        ans, curr = 0, head
        while curr:
            ans = (ans << 1) + curr.val
            curr = curr.next
        return ans


# Test cases
if __name__ == "__main__":
    # Example test case
    head = ListNode(1, ListNode(0, ListNode(1)))
    sol = Solution()
    print(sol.getDecimalValue(head))  # Output: 5

    # Additional test cases
    head2 = ListNode(0)
    print(sol.getDecimalValue(head2))  # Output: 0

    head3 = ListNode(1, ListNode(1, ListNode(1)))
    print(sol.getDecimalValue(head3))  # Output: 7
