class Solution(object):
    def maxAdjacentDistance(self, nums):
        diff = abs(nums[-1] - nums[0])
        for i in range(1, len(nums)):
            diff = max(diff, abs(nums[i] - nums[i - 1]))
        return diff


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3, 6, 10, 15]
    print(sol.maxAdjacentDistance(nums1))  # Output: 5 (10 - 15)
    nums2 = [1, 2, 3, 4, 5]
    print(sol.maxAdjacentDistance(nums2))  # Output: 1 (5 - 4)
    nums3 = [10, 20, 30, 40]
    print(sol.maxAdjacentDistance(nums3))  # Output: 10 (40 - 30)
