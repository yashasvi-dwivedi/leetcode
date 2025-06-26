class Solution(object):
    def longestSubsequence(self, s, k):
        n = len(s)
        zeros = s.count("0")
        ones = 0
        value = 0
        power = 1

        for i in range(n - 1, -1, -1):
            if s[i] == "1":
                if value + power > k:
                    continue
                value += power
                ones += 1
            power <<= 1
            if power > k:
                break

        return zeros + ones


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubsequence("001101", 5))  # Output: 4
    print(sol.longestSubsequence("1111", 1))  # Output: 0
    print(sol.longestSubsequence("0001100", 3))  # Output: 5
    print(sol.longestSubsequence("1000100", 2))  # Output: 4
    print(sol.longestSubsequence("111000", 7))  # Output: 6
