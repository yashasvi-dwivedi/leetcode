class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        n = len(nums)
        diff = [0] * (n + 1)
        result = []

        for i in range(n):
            if nums[i] == key:
                start = max(0, i - k)
                end = min(n, i + k + 1)
                diff[start] += 1
                if end < n:
                    diff[end] -= 1

        s = 0
        for i in range(n):
            s += diff[i]
            if s > 0:
                result.append(i)

        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.findKDistantIndices([1, 2, 3, 4, 5], 3, 1))  # Expected: [2, 1, 3]
    print(sol.findKDistantIndices([1, 2, 3, 4, 5], 6, 1))  # Expected: []
    print(sol.findKDistantIndices([1, 2, 3, 4, 5], 2, 2))  # Expected: [0, 1, 2, 3]
    print(sol.findKDistantIndices([1, 2, 3], 1, 0))  # Expected: [0]
    print(sol.findKDistantIndices([1], 1, 0))  # Expected: [0]
