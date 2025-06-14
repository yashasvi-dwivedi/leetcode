class Solution:
    def minMaxDifference(self, num):
        s = str(num)

        max_s = s
        for ch in s:
            if ch != "9":
                max_s = s.replace(ch, "9")
                break

        min_s = s
        for ch in s:
            if ch != "0":
                min_s = s.replace(ch, "0")
                break

        return int(max_s) - int(min_s)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.minMaxDifference(123456))  # Output: 876543
    print(sol.minMaxDifference(1001))  # Output: 9000
    print(sol.minMaxDifference(9))  # Output: 0
    print(sol.minMaxDifference(123456789))  # Output: 876543210
    print(sol.minMaxDifference(1000000))  # Output: 9000000
