class Solution(object):
    def possibleStringCount(self, word):
        n = len(word)
        count = n
        for i in range(1, n):
            if word[i] != word[i - 1]:
                count -= 1
        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.possibleStringCount("abcde"))  # Output: 5
    print(solution.possibleStringCount("aabbcc"))  # Output: 3
    print(solution.possibleStringCount("aaaaaa"))  # Output: 6
    print(solution.possibleStringCount("ababab"))  # Output: 6
    print(solution.possibleStringCount("xyzxyz"))  # Output: 6
