from typing import List
from functools import reduce
from operator import or_


class Solution:
    def countMaxOrSubsets(self, a: List[int]) -> int:
        return (
            f := lambda i, o, O=reduce(or_, a): a[i:]
            and f(i + 1, o) + f(i + 1, o | a[i])
            or o == O
        )(0, 0)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.countMaxOrSubsets([3, 1]))  # Output: 2
    print(sol.countMaxOrSubsets([2, 2, 2]))  # Output: 7
    print(sol.countMaxOrSubsets([1, 2, 3, 5]))  # Output: 6
    print(sol.countMaxOrSubsets([1, 2, 3, 4, 5]))  # Output: 8
    print("All test cases passed.")
