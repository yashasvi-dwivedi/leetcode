class Solution(object):
    def divideString(self, s, k, fill):
        n = len(s)
        groups = (n + k - 1) // k
        result = []

        for i in range(groups):
            group = ""
            for j in range(k):
                index = i * k + j
                if index < n:
                    group += s[index]
                else:
                    group += fill
            result.append(group)

        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.divideString("abcdefghi", 3, "x"))  # Expected: ['abc', 'def', 'ghi']
    print(sol.divideString("abcdefgh", 3, "x"))  # Expected: ['abc', 'def', 'ghx']
    print(sol.divideString("a", 2, "x"))  # Expected: ['ax']
    print(sol.divideString("", 3, "x"))  # Expected: ['xxx']
    print(sol.divideString("hello", 2, "x"))  # Expected: ['he', 'll', 'ox']
