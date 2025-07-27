from typing import List
from itertools import groupby


class Solution:
    def countHillValley(self, a: List[int]) -> int:
        b = [v for v, _ in groupby(a)]
        return sum(l > m < r or l < m > r for l, m, r in zip(b, b[1:], b[2:]))


# Test cases
def test_countHillValley():
    sol = Solution()
    assert sol.countHillValley([2, 4, 1, 1, 6, 5]) == 3
    assert sol.countHillValley([6, 6, 5, 5, 4, 1]) == 0
    assert sol.countHillValley([1, 2, 3]) == 0
    assert sol.countHillValley([3, 2, 1]) == 0
    assert sol.countHillValley([1, 3, 2]) == 1
    print("All test cases passed.")
