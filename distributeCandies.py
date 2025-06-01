class Solution(object):
    def distributeCandies(self, n, limit):
        res = 0
        for i in range(min(limit, n) + 1):
            if n - i <= 2 * limit:
                res += min(n - i, limit) - max(0, n - i - limit) + 1
        return res


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.distributeCandies(5, 2))  # Example test case
    print(sol.distributeCandies(10, 3))  # Another test case
    print(sol.distributeCandies(7, 4))  # Additional test case
    print(sol.distributeCandies(0, 0))  # Edge case with zero candies and limit
    print(sol.distributeCandies(1, 1))  # Edge case with one candy and limit
