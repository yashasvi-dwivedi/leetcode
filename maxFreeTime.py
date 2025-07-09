class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        s, e, t = startTime, endTime, eventTime

        # Calculate free time gaps
        q = [s[0] - 0]
        for i in range(1, len(s)):
            q.append(s[i] - e[i - 1])
        q.append(t - e[-1])

        # Sliding window of size k+1
        max_free = total = sum(q[: k + 1])
        for i in range(k + 1, len(q)):
            total += q[i] - q[i - k - 1]
            if total > max_free:
                max_free = total

        return max_free


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxFreeTime(10, 2, [1, 2, 3], [2, 3, 4]))
    print(sol.maxFreeTime(10, 1, [1, 2, 3], [2, 3, 4]))
    print(sol.maxFreeTime(10, 2, [1, 2, 6], [10, 5, 8]))
    print(sol.maxFreeTime(20, 1, [1, 11], [10, 20]))
