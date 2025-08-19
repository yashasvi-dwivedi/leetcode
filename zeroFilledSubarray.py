class Solution:
    def zeroFilledSubarray(self, nums):
        count, streak = 0, 0
        for num in nums:
            if num == 0:
                streak += 1
                count += streak
            else:
                streak = 0
        return count


if __name__ == "__main__":
    print("Enter a list of numbers: ")
    nums = list(map(int, input().split()))
    print("Output: ", Solution().zeroFilledSubarray(nums))
