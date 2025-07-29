from typing import List
from itertools import accumulate


class Solution:
    def smallestSubarrays(self, a: List[int]) -> List[int]:
        return [
            *map(
                lambda d: max(d.values()) - d[-1] + 1,
                accumulate(
                    range(len(a) - 1, -1, -1),
                    lambda d, i: d
                    | {q: i for q in range(32) if a[i] & 1 << q}
                    | {-1: i},
                    initial={-1: 0},
                ),
            )
        ][:0:-1]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestSubarrays([1, 2, 3, 4]))  # Example test case
    print(sol.smallestSubarrays([5, 1, 2, 3]))  # Another test case
    print(sol.smallestSubarrays([0, 0, 0]))  # Edge case with all zeros
    print(sol.smallestSubarrays([7, 8, 9]))  # Mixed values
