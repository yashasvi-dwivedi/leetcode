class solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10


# Example usage
if __name__ == "__main__":
    s = solution()
    print(s.isPalindrome(121))  # Output: True
    print(s.isPalindrome(-121))  # Output: False
    print(s.isPalindrome(10))  # Output: False
    print(s.isPalindrome(12321))  # Output: True
