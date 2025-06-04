class Soltuion(object):
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word

        res = ""
        length = len(word) - numFriends + 1
        for i in range(0, len(word)):
            temp = word[i : i + length]
            if temp > res:
                res = temp
        return res


# Test Cases
if __name__ == "__main__":
    solution = Soltuion()
    print(solution.answerString("abacaba", 3))  # Expected: "abac"
    print(solution.answerString("abcde", 2))  # Expected: "cde"
    print(solution.answerString("aaaaa", 1))  # Expected: "aaaaa"
    print(
        solution.answerString("xyz", 4)
    )  # Expected: "xyz" (since numFriends > len(word))
    print(
        solution.answerString("hello", 5)
    )  # Expected: "hello" (since numFriends == len(word))
