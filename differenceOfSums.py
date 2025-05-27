class Solution(object):
    def differenceOfSums(self, n, m):
        totalSum = n * (n + 1) // 2  # Applying formula to sum (1, n)
        divsibleSum = (
            m * (n // m) * (n // m + 1)
        )  # Formula to get the sum of all divisible numbers
        return totalSum - divsibleSum


# Test Cases
if __name__ == "__main__":
    n = 10
    m = 3
    s = Solution()
    result = s.differenceOfSums(n, m)
    print(result)  # Output : 19
    n = 5
    m = 6
    s = Solution()
    result = s.differenceOfSums(n, m)
    print(result)  # Output: 15
    n = 5
    m = 1
    result = s.differenceOfSums(n, m)
    print(result)  # Output: -15
