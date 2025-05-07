class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    print(solution.containsDuplicate(nums))  # Output: True

    nums = [1, 2, 3, 4]
    print(solution.containsDuplicate(nums))  # Output: False

    nums = [1, 2, 3, 1, 2, 3]
    print(solution.containsDuplicate(nums))  # Output: True
