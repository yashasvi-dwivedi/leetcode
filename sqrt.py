class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    x = 8
    result = solution.mySqrt(x)
    print(f"The square root of {x} is approximately {result}.")
