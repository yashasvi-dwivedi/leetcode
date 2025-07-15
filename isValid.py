class Solution(object):
    def isValid(self, s):
        if len(s) > 3:
            return False

        vowels = 0
        consonants = 0
        vowel_set = "aeiouAEIOU"

        for c in s:
            if c.isalpha():
                if c in vowel_set:
                    vowels += 1
                else:
                    consonants += 1
            elif not c.isdigit():
                return False

        return vowels >= 1 and consonants >= 1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("a1b2"))
    print(solution.isValid("abc"))
    print(solution.isValid("a1"))
    print(solution.isValid("1a2b"))
    print(solution.isValid("123"))
    print(solution.isValid("a"))
    print(solution.isValid("A1B2C3"))
    print(solution.isValid("!@#"))
