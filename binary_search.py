class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# Example usage
if __name__ == "__main__":
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))  # Output: 4
    print(s.search([-1, 0, 3, 5, 9, 12], 2))  # Output: -1
    print(s.search([], 0))  # Output: -1
    print(s.search([1], 1))  # Output: 0
