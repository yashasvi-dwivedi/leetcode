class Solution(object):
    def differenceOfSums(self, n, m):
        totalSum = n * (n + 1) // 2
        divsibleSum = m * (n // m) * (n // m + 1)
        return totalSum - divsibleSum


if __name__ == "__main__":
    n = 10
    m = 3
    s = Solution()
    result = s.differenceOfSums(n, m)
    print(result)
    n = 5
    m = 6
    s = Solution()
    result = s.differenceOfSums(n, m)
    print(result)
    n = 5
    m = 1
    result = s.differenceOfSums(n, m)
    print(result)
