class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


# Test the function
if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(strs)
    print(result)  # Expected output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
