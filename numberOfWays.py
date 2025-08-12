from functools import cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        p = [q**x for q in range(1, round(n ** (1 / x)) + 1)]

        @cache
        def f(i, n):
            if i < len(p) and n >= p[i]:
                return (f(i + 1, n) + f(i + 1, n - p[i])) % (10**9 + 7)
            return int(n == 0)

        return f(0, n)


# Test cases
sol = Solution()
print(sol.numberOfWays(5, 2))  # Example test case
print(sol.numberOfWays(10, 2))  # Example test case
print(sol.numberOfWays(10, 3))  # Example test case
