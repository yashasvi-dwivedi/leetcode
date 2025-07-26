class Solution:
    def maxSubarrays(self, n: int, conflictingPairs) -> int:
        from collections import defaultdict

        right = defaultdict(list)
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))

        left = [0, 0]
        bonus = [0] * (n + 1)
        ans = 0

        for r in range(1, n + 1):
            for l in right[r]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]

            ans += r - left[0]
            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]

        return ans + max(bonus)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubarrays(5, [[1, 2], [2, 3], [4, 5]]))  # Example test case
    print(solution.maxSubarrays(3, [[1, 2], [2, 3]]))  # Another test case
    print(solution.maxSubarrays(4, [[1, 2], [3, 4], [1, 3]]))  # Yet another test case
