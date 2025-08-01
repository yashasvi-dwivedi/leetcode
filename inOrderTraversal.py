from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )


# Test cases
if __name__ == "__main__":
    # Example tree: [1, None, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    print(solution.inorderTraversal(root))  # Output: [1, 3, 2]

    # Empty tree
    empty_root = None
    print(solution.inorderTraversal(empty_root))  # Output: []
