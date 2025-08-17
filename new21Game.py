class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * maxPts
        dp[0] = 1.0

        window_sum = 1.0
        result = 0.0

        for i in range(1, n + 1):
            prob = window_sum / maxPts

            if i < k:
                window_sum += prob
            else:
                result += prob

            if i >= maxPts:
                window_sum -= dp[i % maxPts]

            dp[i % maxPts] = prob

        return result


# Test cases

print(Solution().new21Game(10, 1, 10))  # Expected output: 1.0
print(Solution().new21Game(6, 1, 10))  # Expected output: 0.6
print(Solution().new21Game(21, 17, 10))  # Expected output: 0.73278
