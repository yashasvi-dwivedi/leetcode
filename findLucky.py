from collections import Counter


class Solution(object):
    def findLucky(self, arr):
        freq = Counter(arr)
        lucky = -1

        for num, count in freq.items():
            if num == count:
                lucky = max(lucky, num)

        return lucky


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findLucky([2, 2, 3, 4]))  # Output: -1
    print(solution.findLucky([1, 2, 2, 3, 3, 3]))  # Output: 3
    print(solution.findLucky([7, 7, 7, 7]))  # Output: 7
    print(solution.findLucky([1, 2, 3, 4]))  # Output: -1
    print(solution.findLucky([]))  # Output: -1
