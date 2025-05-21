class Solution(object):
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


# Test the function
if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    encoded = solution.encode(strs)
    print("Encoded:", encoded)  # Encoded string
    decoded = solution.decode(encoded)
    print(
        "Decoded:", decoded
    )  # Expected output: ["eat", "tea", "tan", "ate", "nat", "bat"]
