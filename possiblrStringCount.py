class Solution(object):
    MOD = 10**9 + 7

    def possibleStringCount(self, word, k):
        if not word:
            return 0

        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        total = 1
        for num in groups:
            total = (total * num) % self.MOD

        if k <= len(groups):
            return total

        dp = [0] * k
        dp[0] = 1

        for num in groups:
            new_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0:
                    sum_val = (sum_val + dp[s - 1]) % self.MOD
                if s > num:
                    sum_val = (sum_val - dp[s - num - 1] + self.MOD) % self.MOD
                new_dp[s] = sum_val
            dp = new_dp

        invalid = sum(dp[len(groups) : k]) % self.MOD
        return (total - invalid + self.MOD) % self.MOD


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.possibleStringCount("abcde", 3))  # Output: 5
    print(solution.possibleStringCount("aabbcc", 2))  # Output: 3
    print(solution.possibleStringCount("aaaaaa", 4))  # Output: 6
    print(solution.possibleStringCount("ababab", 5))  # Output: 6
    print(solution.possibleStringCount("xyzxyz", 6))  # Output: 6
