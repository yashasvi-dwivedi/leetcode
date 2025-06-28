from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        if k >= len(nums):
            return sorted(nums)

        # Create a list of tuples (value, index)
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # Sort by value in descending order
        indexed_nums.sort(reverse=True, key=lambda x: x[0])

        # Select the first k elements and sort them by their original indices
        selected = sorted(indexed_nums[:k], key=lambda x: x[1])

        # Return only the values
        return [num for num, _ in selected]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubsequence([3, 4, 3, 2], 2))  # Output: [3, 4]
    print(sol.maxSubsequence([2, 1, 3], 2))  # Output: [2, 3]
    print(sol.maxSubsequence([1, 2, 3], 0))  # Output: []
    print(sol.maxSubsequence([5, 6, 7], 5))  # Output: [5, 6, 7]
