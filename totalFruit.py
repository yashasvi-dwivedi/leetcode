from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last = second_last = -1
        last_count = curr = res = 0

        for f in fruits:
            if f == last or f == second_last:
                curr += 1
            else:
                curr = last_count + 1

            if f == last:
                last_count += 1
            else:
                last_count = 1
                second_last, last = last, f

            res = max(res, curr)

        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.totalFruit([1, 2, 1]))  # Output: 3
    print(solution.totalFruit([0, 1, 2, 2]))  # Output: 3
    print(solution.totalFruit([1, 2, 3, 2, 2]))  # Output: 4
    print(solution.totalFruit([3, 3, 3, 1, 2, 1, 1]))  # Output: 5
