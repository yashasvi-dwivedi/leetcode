class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        j = 0
        maxLength = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                maxLength = max(maxLength, i - j + 1)
        return maxLength


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findLHS([1, 3, 2, 2, 5, 4, 3]))
    print(solution.findLHS([1, 2, 3, 4]))
    print(solution.findLHS([1, 1, 1, 1]))
    print(solution.findLHS([1, 2, 2, 3, 3]))
