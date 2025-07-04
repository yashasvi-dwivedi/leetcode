class Solution(object):
    def longestCommonPrefix(self, strs):
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""

                pref = pref[0:pref_len]

        return pref


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""
    print(solution.longestCommonPrefix(["a"]))  # Output: "a"
    print(solution.longestCommonPrefix([""]))  # Output: ""
    print(solution.longestCommonPrefix(["ab", "a"]))  # Output: "a"
