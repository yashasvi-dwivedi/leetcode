class Solution(object):
    def romanToInt(self, s):
        table = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sm, pre = 0, "I"
        for c in s[::-1]:
            if table[c] < table[pre]:
                sm, pre = sm - table[c], c
            else:
                sm, pre = sm + table[c], c
        return sm


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))  # Output: 3
    print(s.romanToInt("IV"))  # Output: 4
    print(s.romanToInt("IX"))  # Output: 9
    print(s.romanToInt("LVIII"))  # Output: 58
    print(s.romanToInt("MCMXCIV"))  # Output: 1994
