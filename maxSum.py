class Solution(object):
    def maxSum(self, nums):
        max_value = max(nums)
        if all(n < 0 for n in nums):
            return max_value

        seen = [False] * 101
        for n in nums:
            if 0 <= n <= 100:
                seen[n] = True

        return sum(i for i, present in enumerate(seen[1:], start=1) if present)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSum([1, 2, 3, 4, 5]))  # Output: 15
    print(sol.maxSum([-1, -2, -3]))  # Output: -1
    print(sol.maxSum([0, 0, 0]))  # Output: 0
    print(sol.maxSum([100, 99, 98]))  # Output: 297
    print(sol.maxSum([101, -1, -2]))  # Output: 0
