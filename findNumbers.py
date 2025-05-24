class Solution(object):
    def findNumber(self, nums):
        count = 0
        for i in nums:
            s = str(i)
            if len(s) % 2 == 0:
                count += 1
        return count


# Test Cases
if __name__ == "__main__":
    nums = [12, 345, 2, 6, 7896]
    s = Solution()
    result = s.findNumber(nums)
    print(result)
