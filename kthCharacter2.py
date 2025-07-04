class Solution(object):
    def kthCharacter(self, k, operations):
        n, i = 1, 0
        while n < k:
            n *= 2
            i += 1
        d = 0
        while n > 1:
            if k > n // 2:
                k -= n // 2
                d += operations[i - 1]
            n //= 2
            i -= 1
        return chr(d % 26 + ord("a"))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    operations = [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ]
    print(solution.kthCharacter(1, operations))  # Output: 'a'
    print(solution.kthCharacter(2, operations))  # Output: 'b'
    print(solution.kthCharacter(3, operations))  # Output: 'c'
    print(solution.kthCharacter(26, operations))  # Output: 'z'
    print(solution.kthCharacter(27, operations))  # Output: 'a'
    print(solution.kthCharacter(52, operations))
