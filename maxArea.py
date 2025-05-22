class Solution(object):
    def maxArea(self, heights):
        left, r = 0, len(heights) - 1
        res = 0

        while left < r:
            area = min(heights[left], heights[r]) * (r - left)
            res = max(res, area)
            if heights[left] <= heights[r]:
                left += 1
            else:
                r -= 1
        return res


# Test the function
if __name__ == "__main__":
    solution = Solution()
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(heights))  # Output: 49
