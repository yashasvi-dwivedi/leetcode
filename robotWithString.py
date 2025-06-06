from collections import Counter


class Solution(object):
    def robotWithString(self, s):
        freq = Counter(s)
        st = []
        res = []

        def min_char(freq):
            for i in range(26):
                ch = chr(ord("a") + i)
                if freq[ch] > 0:
                    return ch
            return "a"

        for ch in s:
            st.append(ch)
            freq[ch] -= 1
            while st and st[-1] <= min_char(freq):
                res.append(st.pop())

        while st:
            res.append(st.pop())

        return "".join(res)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.robotWithString("zza"))  # Expected: "azz"
    print(solution.robotWithString("bac"))  # Expected: "abc"
    print(solution.robotWithString("cba"))  # Expected: "abc"
    print(solution.robotWithString("leetcode"))  # Expected: "cdelotee"
    print(solution.robotWithString("abacabadabacaba"))  # Expected: "aaaaabbbccdd"
