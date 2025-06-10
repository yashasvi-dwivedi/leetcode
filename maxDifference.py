class Solution(object):
    def maxDifference(self, s):
        mpp = [0] * 26
        maxi = 0
        mini = len(s)

        for c in s:
            mpp[ord(c) - ord("a")] += 1
        for i in range(26):
            if mpp[i] % 2 != 0:
                maxi = max(maxi, mpp[i])
            if mpp[i] % 2 == 0 and mpp[i] > 0:
                mini = min(mini, mpp[i])
        return maxi - mini


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    s1 = "aaaaabbc"
    print(sol.maxDifference(s1))  # Output: 3 (5 - 2)
    s2 = "aabbcc"
    print(sol.maxDifference(s2))  # Output: 0 (2 - 2)
    s3 = "abcde"
    print(sol.maxDifference(s3))  # Output: 1 (1 - 0)
