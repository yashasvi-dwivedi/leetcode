import heapq


class Solution(object):
    def minTimeToReach(self, moveTime):
        n = len(moveTime)
        m = len(moveTime[0])
        INF = float("inf")
        dp = [[INF] * m for _ in range(n)]
        minh = [(0, 0, 0)]
        moveTime[0][0] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while minh:
            currTime, currRow, currCol = heapq.heappop(minh)

            if currTime >= dp[currRow][currCol]:
                continue
            if currRow == n - 1 and currCol == m - 1:
                return currTime

            dp[currRow][currCol] = currTime

            for dr, dc in directions:
                nextRow = currRow + dr
                nextCol = currCol + dc
                if (
                    0 <= nextRow < n
                    and 0 <= nextCol < m
                    and dp[nextRow][nextCol] == INF
                ):
                    cost = (currRow + currCol) % 2 + 1
                    start = max(moveTime[nextRow][nextCol], currTime)
                    nextTime = start + cost
                    heapq.heappush(minh, (nextTime, nextRow, nextCol))

        return -1


# Example usage
if __name__ == "__main__":
    s = Solution()
    moveTime = [[0, 2], [1, 3]]
    print(s.minTimeToReach(moveTime))
    moveTime = [[0, 2], [1, 3], [2, 4]]
    print(s.minTimeToReach(moveTime))
    moveTime = [[0, 2], [1, 3], [2, 4], [3, 5]]
    print(s.minTimeToReach(moveTime))
