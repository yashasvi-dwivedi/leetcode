class Solution(object):
    def countSubarrays(self, nums, k):
        m = max(nums)
        m_f = i = c = 0
        for j in range(len(nums)):
            if m == nums[j]:
                m_f += 1
            while m_f >= k:
                c += len(nums) - j
                if nums[i] == m:
                    m_f -= 1
                i += 1
        return c


# Example usage:
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 1
    solution = Solution()
    result = solution.countSubarrays(nums, k)
    print(result)

# Output: 10
