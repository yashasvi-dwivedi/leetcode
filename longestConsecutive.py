class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


# Test the function
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    result = solution.longestConsecutive(nums)
    print(result)  # Output: 4
    nums = [0, 0, 1]
    solution = Solution()
    result = solution.longestConsecutive(nums)
    print(result)  # Output: 2
