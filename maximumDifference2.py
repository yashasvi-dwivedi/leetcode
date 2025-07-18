import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  # or raise an error, depending on requirements

        k = n // 3

        # Step 1: Build prefix sums using max-heap
        maxHeap = []
        prefix = [0] * n
        sum_ = 0

        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
            sum_ += nums[i]
        prefix[k - 1] = sum_

        for i in range(k, 2 * k):
            if -maxHeap[0] > nums[i]:
                sum_ = prefix[i - 1] - (-heapq.heappop(maxHeap)) + nums[i]
                heapq.heappush(maxHeap, -nums[i])
                prefix[i] = sum_
            else:
                prefix[i] = prefix[i - 1]

        # Step 2: Build suffix sums using min-heap
        minHeap = []
        suffix = [0] * n
        sum_ = 0

        for i in range(n - 1, n - k - 1, -1):
            heapq.heappush(minHeap, nums[i])
            sum_ += nums[i]
        suffix[n - k] = sum_

        for i in range(n - k - 1, k - 1, -1):
            if minHeap[0] < nums[i]:
                sum_ = suffix[i + 1] - heapq.heappop(minHeap) + nums[i]
                heapq.heappush(minHeap, nums[i])
                suffix[i] = sum_
            else:
                suffix[i] = suffix[i + 1]

        ans = float("inf")
        for i in range(k - 1, 2 * k):
            ans = min(ans, prefix[i] - suffix[i + 1])

        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDifference([3, 9, 7, 3]))  # Example test case
    print(solution.minimumDifference([1, 2, 3, 4, 5, 6]))  # Even length
    print(solution.minimumDifference([1, 1, 1, 1]))  # All same elements
    print(solution.minimumDifference([10, 20, 30, 40]))  # Distinct elements
    print(solution.minimumDifference([5]))  # Single element
    print(solution.minimumDifference([]))  # Empty list
