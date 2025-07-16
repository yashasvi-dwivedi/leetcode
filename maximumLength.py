class Solution:
    def maximumLength(self, nums):
        count_even = 0
        count_odd = 0
        for num in nums:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

        even_dp = 0
        odd_dp = 0
        for num in nums:
            if num % 2 == 0:
                even_dp = max(even_dp, odd_dp + 1)
            else:
                odd_dp = max(odd_dp, even_dp + 1)

        return max(count_even, count_odd, even_dp, odd_dp)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLength([1, 2, 3, 4, 5]))  # Example test case
    print(solution.maximumLength([2, 4, 6]))  # All even
    print(solution.maximumLength([1, 3, 5]))  # All odd
    print(solution.maximumLength([1, 2, 3, 4]))  # Mixed
    print(solution.maximumLength([]))  # Empty list
    print(solution.maximumLength([1]))  # Single odd number
    print(solution.maximumLength([2]))  # Single even number
