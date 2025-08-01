# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isTreeSymmetric(self, leftRoot, rightRoot):
        if leftRoot is None and rightRoot is None:
            return True
        if (leftRoot is None and rightRoot is not None) or (
            leftRoot is not None and rightRoot is None
        ):
            return False
        return self.isTreeSymmetric(
            leftRoot.left, rightRoot.right
        ) and self.isTreeSymmetric(leftRoot.right, rightRoot.left)

    def isSymmetric(self, root):
        return self.isTreeSymmetric(root.left, root.right)


# Test cases
if __name__ == "__main__":
    # Example usage:
    # Constructing a symmetric tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    solution = Solution()
    print(solution.isSymmetric(root))  # Output: True

    # Constructing a non-symmetric tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)

    print(solution.isSymmetric(root2))  # Output: False
