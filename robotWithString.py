from collections import Counter


class Solution(object):
    def robotWithString(self, s):
        freq = Counter(s)  # Count the frequency of each character in the string
        st = []  # Stack to simulate the robot's holding area
        res = []  # Result list to build the output string

        # Helper function to find the smallest character still available in freq
        def min_char(freq):
            for i in range(26):  # Loop through 'a' to 'z'
                ch = chr(ord("a") + i)
                if freq[ch] > 0:
                    return ch  # Return the smallest available character
            return "a"  # Default return (should not be reached)

        # Process each character in the input string
        for ch in s:
            st.append(ch)  # Push the character onto the stack
            freq[ch] -= 1  # Decrement its frequency
            # While the top of the stack is <= the smallest remaining character, pop to result
            while st and st[-1] <= min_char(freq):
                res.append(st.pop())

        # Pop any remaining characters from the stack to the result
        while st:
            res.append(st.pop())

        return "".join(res)  # Join the result list into a string


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.robotWithString("zza"))  # Expected: "azz"
    print(solution.robotWithString("bac"))  # Expected: "abc"
    print(solution.robotWithString("cba"))  # Expected: "abc"
    print(solution.robotWithString("leetcode"))  # Expected: "cdelotee"
    print(solution.robotWithString("abacabadabacaba"))  # Expected: "aaaaabbbccdd"
