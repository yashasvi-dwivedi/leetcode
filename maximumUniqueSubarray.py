class Solution:
    def maximumUniqueSubarray(self, nums):
        res = 0
        cur_sum = 0
        start = 0
        seen = set()

        for end in range(len(nums)):
            while nums[end] in seen:
                seen.remove(nums[start])
                cur_sum -= nums[start]
                start += 1

            cur_sum += nums[end]
            seen.add(nums[end])

            res = max(res, cur_sum)

        return res


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumUniqueSubarray([4, 2, 1, 2, 3, 5]))  # Output: 11
    print(sol.maximumUniqueSubarray([1, 2, 3, 4, 5]))  # Output: 15
    print(sol.maximumUniqueSubarray([1, 1, 1, 1]))  # Output: 1
    print(sol.maximumUniqueSubarray([5, 6, 7, 8, 9]))  # Output: 35
    print(sol.maximumUniqueSubarray([10, 20, 10, 30]))  # Output: 60
