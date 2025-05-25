class Solution(object):
    def longestConsecutive(self, nums):
        # Convert the list to a set for O(1) lookups
        numSet = set(nums)
        longest = 0  # Variable to keep track of the longest sequence found

        # Iterate through each unique number in the set
        for num in numSet:
            # Only start counting if 'num' is the start of a sequence
            if (num - 1) not in numSet:
                length = 1  # Start with the current number
                # Count consecutive numbers
                while (num + length) in numSet:
                    length += 1
                # Update the longest sequence length if needed
                longest = max(length, longest)
        return longest  # Return the length of the longest consecutive sequence


# Test the function
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    result = solution.longestConsecutive(nums)
    print(result)  # Output: 4

    nums = [0, 0, 1]
    solution = Solution()
    result = solution.longestConsecutive(nums)
    print(result)  # Output: 2
