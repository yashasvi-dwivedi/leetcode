class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0]
        last = s[0]
        count = 1

        for i in range(1, len(s)):
            if s[i] != last:
                last = s[i]
                count = 0

            count += 1
            if count > 2:
                continue

            result += s[i]

        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.makeFancyString("leeetcode"))  # Output: "leetcode"
    print(sol.makeFancyString("aaabaaaa"))  # Output: "aabaa"
    print(sol.makeFancyString("aab"))  # Output: "aab"
    print(sol.makeFancyString("aaa"))  # Output: "aa"
    print(sol.makeFancyString("abcde"))  # Output: "abcde"
