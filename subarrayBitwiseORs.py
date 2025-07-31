class Solution(object):
    def subarrayBitwiseORs(self, arr):
        res = set()
        cur = set()
        for num in arr:
            cur = {num | x for x in cur} | {num}
            res |= cur
        return len(res)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarrayBitwiseORs([1, 2, 3]))  # Output: 6
    print(sol.subarrayBitwiseORs([1, 1, 2]))  # Output: 3
    print(sol.subarrayBitwiseORs([1, 2, 4]))  # Output: 6
    print(sol.subarrayBitwiseORs([0]))  # Output: 1
