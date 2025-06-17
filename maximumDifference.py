class Solution(object):
    def maximumDifference(self, nums):
        ans = -1
        mx = -1

        n = len(nums)
        i = n - 1

        while i >= 0:
            ans = max(ans, mx - nums[i])
            mx = max(mx, nums[i])
            i -= 1

        if ans == 0:
            return -1
        else:
            return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumDifference([1, 2, 3, 4, 5]))  # Output: 4
    print(solution.maximumDifference([5, 4, 3, 2, 1]))  # Output: -1
    print(solution.maximumDifference([1, 5, 2, 10]))  # Output: 9
    print(solution.maximumDifference([10, 20, 30]))  # Output: 20
    print(solution.maximumDifference([1]))  # Output: -1
