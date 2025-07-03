class Solution(object):
    def kthCharacter(self, k):
        sb = ["a"]
        while len(sb) < k:
            size = len(sb)
            for i in range(size):
                next_char = chr(ord("a") + ((ord(sb[i]) - ord("a") + 1) % 26))
                sb.append(next_char)
        return sb[k - 1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.kthCharacter(1))  # Output: 'a'
    print(solution.kthCharacter(2))  # Output: 'b'
    print(solution.kthCharacter(3))  # Output: 'c'
    print(solution.kthCharacter(26))  # Output: 'z'
    print(solution.kthCharacter(27))  # Output: 'a'
    print(solution.kthCharacter(52))  # Output: 'z'
    print(solution.kthCharacter(53))  # Output: 'a'
