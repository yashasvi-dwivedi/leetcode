class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for idx in set(s):
            if s.count(idx) != t.count(idx):
                return False
        return True


# Example usage
if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))  # Output: True
    print(s.isAnagram("rat", "car"))  # Output: False
    print(s.isAnagram("a", "ab"))  # Output: False
    print(s.isAnagram("", ""))  # Output: True
