class Solution(object):
    def createPalindrome(self, num, odd):
        x = num
        if odd:
            x //= 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num

    def isPalindrome(self, num, base):
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]

    def kMirror(self, k, n):
        total = 0
        length = 1
        while n > 0:
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, True)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, False)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            length *= 10
        return total


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.kMirror(2, 5))  # Expected: 25 (1 + 3 + 5 + 7 + 9)
    print(sol.kMirror(3, 5))  # Expected: 21 (1 + 2 + 3 + 4 + 5)
    print(sol.kMirror(4, 5))  # Expected: 15 (1 + 2 + 3 + 4 + 5)
    print(sol.kMirror(10, 5))  # Expected: 15 (1 + 2 + 3 + 4 + 5)
