class Solution(object):
    def isPowerTwo(self, n):
        return n > 0 and not (n & (n - 1))


if __name__ == "__main__":
    print("Provide a value for n")
    n = int(input())
    print(Solution().isPowerTwo(n))
