class Solution(object):
    def twoSum(self, nums, target):
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [pair_idx[target - num], i]
            pair_idx[num] = i
        return []


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]
