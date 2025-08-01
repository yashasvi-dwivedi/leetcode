class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        max_area = 0
        stack = []

        for i in range(n + 1):
            curr_height = 0 if i == n else heights[i]

            while stack and curr_height < heights[stack[-1]]:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                area = heights[top] * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # Output: 10
    print(solution.largestRectangleArea([2, 4]))  # Output: 4
    print(solution.largestRectangleArea([1]))  # Output: 1
    print(solution.largestRectangleArea([5, 4, 1, 2]))  # Output: 8
