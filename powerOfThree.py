class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfThree(27))  # True
    print(sol.isPowerOfThree(0))  # False
    print(sol.isPowerOfThree(9))  # True
    print(sol.isPowerOfThree(45))  # False
