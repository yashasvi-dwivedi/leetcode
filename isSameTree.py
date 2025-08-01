from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


# Test cases
if __name__ == "__main__":
    # Example trees
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    solution = Solution()
    print(solution.isSameTree(tree1, tree2))  # Output: True

    # Different trees
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)

    print(solution.isSameTree(tree1, tree3))  # Output: False
