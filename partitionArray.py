class Solution(object):
    def partitionArray(self, nums, k):
        nums.sort()
        ans = 1
        min_val = nums[0]
        for num in nums[1:]:
            if num - min_val > k:
                ans += 1
                min_val = num
        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionArray([3, 6, 1, 2, 5], 2))  # Output: 2
    print(solution.partitionArray([1, 2, 3], 0))  # Output: 3
    print(solution.partitionArray([1, 5, 10, 15], 3))  # Output: 2
    print(solution.partitionArray([1, 3, 6, 7, 9], 2))  # Output: 3
