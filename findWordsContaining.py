class Solution(object):
    def findWordsContaining(self, words, x):
        res = []  # Intialize an empty list

        for i in range(len(words)):  # Start a loop through length of words
            a = words[i]  # Assign index of words to a variable
            if x in a:
                res.append(i)  # Check if x appears in a , if it does append it to res
        return res  # Return res


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
