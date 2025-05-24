class Solution(object):
    def findWordsContaining(self, words, x):
        res = []

        for i in range(len(words)):
            a = words[i]
            if x in a:
                res.append(i)
        return res


# Test Cases
if __name__ == "__main__":
    words = ["leet", "code"]
    x = "e"
    s = Solution()
    result = s.findWordsContaining(words, x)
    print(result)  # Output: [0, 1]
    words = ["abc", "bcd", "aaaa", "cbc"]
    x = "a"
    s = Solution()
    result = s.findWordsContaining(words, x)
    print(result)  # Output: [0, 2]
    words = ["abc", "bcd", "aaaa", "cbc"]
    x = "z"
    s = Solution()
    result = s.findWordsContaining(words, x)
    print(result)  # Output: []
