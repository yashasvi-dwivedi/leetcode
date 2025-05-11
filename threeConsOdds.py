class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        for i in arr:
            if i & 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False


# Test the function
if __name__ == "__main__":
    arr = [2, 6, 4, 1]
    sol = Solution()
    print(sol.threeConsecutiveOdds(arr))  # Output: False

    arr = [1, 2, 3, 4]
    print(sol.threeConsecutiveOdds(arr))  # Output: False

    arr = [1, 3, 5, 7]
    print(sol.threeConsecutiveOdds(arr))  # Output: True
