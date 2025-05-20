class Solution(object):
    def triangleType(self, nums):
        if (
            nums[0] + nums[1] <= nums[2]
            or nums[1] + nums[2] <= nums[0]
            or nums[0] + nums[2] <= nums[1]
        ):
            return None

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"

        elif nums[0] != nums[1] != nums[2] and nums[0] != nums[2] != nums[1]:
            return "scalene"
        else:
            return "isoceles"


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1]
    result = solution.triangleType(nums)
    print(f"The triangle type is {result}.")

    nums = [2, 2, 3]
    result = solution.triangleType(nums)
    print(f"The triangle type is {result}.")

    nums = [3, 4, 5]
    result = solution.triangleType(nums)
    print(f"The triangle type is {result}.")
    nums = [1, 2, 3]
    result = solution.triangleType(nums)
    print(f"The triangle type is {result}.")
