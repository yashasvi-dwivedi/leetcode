class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)

        # Bước 1: Tính khoảng trống giữa các meeting
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[n - 1]

        # Bước 2: Tiền xử lý maxLeft và maxRight
        maxLeft = [0] * (n + 1)
        maxLeft[0] = gaps[0]
        for i in range(1, n + 1):
            maxLeft[i] = max(maxLeft[i - 1], gaps[i])

        maxRight = [0] * (n + 1)
        maxRight[n] = gaps[n]
        for i in range(n - 1, -1, -1):
            maxRight[i] = max(maxRight[i + 1], gaps[i])

        # Bước 3: Duyệt từng meeting và tính kết quả
        res = 0
        for i in range(n):
            duration = endTime[i] - startTime[i]
            gap_sum = gaps[i] + gaps[i + 1]

            bestGap = 0
            if i > 0:
                bestGap = max(bestGap, maxLeft[i - 1])
            if i + 2 <= n:
                bestGap = max(bestGap, maxRight[i + 2])

            if duration <= bestGap:
                res = max(res, gap_sum + duration)
            else:
                res = max(res, gap_sum)

        return res


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxFreeTime(10, [1, 2, 3], [2, 3, 4]))  # Example test case
    print(sol.maxFreeTime(10, [1, 2, 6], [10, 5, 8]))  # Example test case
    print(sol.maxFreeTime(20, [1, 11], [10, 20]))  # Example test case
    print(sol.maxFreeTime(15, [1, 5, 7], [3, 6, 10]))  # Example test case
