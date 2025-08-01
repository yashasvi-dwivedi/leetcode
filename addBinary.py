class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(s))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("11", "1"))  # Output: "100"
    print(solution.addBinary("1010", "1011"))  # Output: "10101"
    print(solution.addBinary("0", "0"))  # Output: "0"
    print(solution.addBinary("1", "1"))  # Output: "10"
