class Solution(object):
    def isPalindrome(self, s):
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


# Test the function
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)  # Output: True
    s = "race a car"
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)  # Output: False
