from typing import List
from collections import Counter
from itertools import product


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0  # Return 0 for empty input

        z = Counter()
        for p in product((v % k for v in nums), range(k)):
            z[p] = z[p[::-1]] + 1

        return max(z.values())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLength([1, 2, 3, 4, 5], 2))  # Example test case
    print(solution.maximumLength([2, 4, 6], 2))  # All even
    print(solution.maximumLength([1, 3, 5], 2))  # All odd
    print(solution.maximumLength([1, 2, 3, 4], 2))  # Mixed
    print(solution.maximumLength([], 2))  # Empty list
    print(solution.maximumLength([1], 2))  # Single odd number
    print(solution.maximumLength([2], 2))  # Single even number
