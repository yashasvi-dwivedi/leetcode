from collections import Counter


class Solution(object):
    def longestPalindrome(self, words):
        # Count the frequency of each word in the list
        mpp = Counter(words)
        count = 0  # Total length of palindrome
        alreadyPalindrome = (
            0  # Flag to check if a single palindromic word can be placed in the center
        )

        # Iterate through each unique word and its frequency
        for w, freq in mpp.items():
            s = w[::-1]  # Reverse of the word
            if w == s:
                # If the word is a palindrome (e.g., "gg"), pair them up
                count += (freq // 2) * 4  # Each pair contributes 4 to the length
                if freq % 2:
                    # If there's an unpaired palindromic word, it can be placed in the center
                    alreadyPalindrome = 1
            elif w < s and s in mpp:
                # For non-palindromic pairs (e.g., "lc" and "cl"), only count once to avoid double counting
                count += min(freq, mpp[s]) * 4  # Each pair contributes 4 to the length
        # Add 2 if there is a single palindromic word to place in the center
        return count + alreadyPalindrome * 2


# Test Cases
if __name__ == "__main__":
    words = ["lc", "cl", "gg"]
    solution = Solution()
    result = solution.longestPalindrome(words)
    print(result)  # Output: 6

    words = ["ab", "ty", "yt", "lc", "cl", "ab"]
    solution = Solution()
    result = solution.longestPalindrome(words)
    print(result)  # Output: 8

    words = ["cc", "ll", "xx"]
    s = Solution()
    result = s.longestPalindrome(words)
    print(result)  # Output: 2
