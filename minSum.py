class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1 = sum(nums1)
        count1 = nums1.count(0)
        sum2 = sum(nums2)
        count2 = nums2.count(0)

        min_sum1 = sum1 + count1
        min_sum2 = sum2 + count2

        if min_sum1 == min_sum2:
            return min_sum1
        elif min_sum1 > min_sum2:
            if count2 > 0:
                return min_sum1
            else:
                return -1
        else:
            if count1 > 0:
                return min_sum2
            else:
                return -1


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0]
    nums2 = [4, 5, 6, 0]
    print(solution.minSum(nums1, nums2))  # Output: 16
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(solution.minSum(nums1, nums2))  # Output: -1
    nums1 = [0, 0, 0]
    nums2 = [0, 0, 0]
    print(solution.minSum(nums1, nums2))  # Output: 0
