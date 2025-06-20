class Solution(object):
    def maxDistance(self, s, k):
        res = 0
        for dirr in "NE", "SE", "SW", "NW":
            kk, dist = k, 0
            for c in s:
                dist += c in dirr or kk > 0 or -1
                kk -= c not in dirr
                res = max(res, dist)

        return res


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s = "NSEW"
    k = 2
    print(sol.maxDistance(s, k))  # Output: 4
    sol = Solution()
    s = "NNNN"
    k = 1
    print(sol.maxDistance(s, k))  # Output: 3
    sol = Solution()
    s = "NNNN"
    k = 2
    print(sol.maxDistance(s, k))  # Output: 4
