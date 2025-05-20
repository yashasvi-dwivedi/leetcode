class Solution(object):
    def isZeroArray(self, nums, queries):
        n = len(nums)
        sweep = [0] * (n + 1)

        for l, r in queries:
            sweep[l] += 1
            if r + 1 <= n:
                sweep[r + 1] -= 1

        for i in range(1, n + 1):
            sweep[i] += sweep[i - 1]

        for i in range(n):
            if sweep[i] < nums[i]:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 4, 5]
    queries = [(0, 1)]
    result = s.isZeroArray(nums, queries)
    print(f"Result: {result}")

    nums = [1, 2, 4, 5]
    queries = [(0, 1), (1, 2)]
    result = s.isZeroArray(nums, queries)
    print(f"Result: {result}")
