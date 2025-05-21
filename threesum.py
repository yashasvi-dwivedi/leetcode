class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            left, r = i + 1, len(nums) - 1
            while left < r:
                threeSum = a + nums[left] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[r]])
                    left += 1
                    r -= 1
                    while left < r and nums[left] == nums[left - 1]:
                        left += 1  # noqa: E741

        return res


# Test the function
if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))  # Expected output: [[-1, -1, 2], [-1, 0, 1]]
