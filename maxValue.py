import bisect


class Solution:
    def maxValue(self, events, k: int):
        N = len(events)
        events.sort()

        memo = [[-1 for _ in range(k + 1)] for _ in range(N)]

        def max_events_recur(idx, k):
            if idx == N or k == 0:
                return 0

            if memo[idx][k] != -1:
                return memo[idx][k]

            startDay, endDay, value = events[idx]

            # Take this event
            # Get the next available event to call recursion on after taking this event
            nextIdxAvail = bisect.bisect_right(
                events, endDay, key=lambda event: event[0]
            )
            total = value + max_events_recur(nextIdxAvail, k - 1)

            # Don't take this event
            total = max(total, max_events_recur(idx + 1, k))

            memo[idx][k] = total
            return total

        total = max_events_recur(0, k)
        # print("memo: ")
        # print(np.array(memo))
        return total

    # Test cases


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxValue([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 2))  # Output: 7
    print(sol.maxValue([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 1))  # Output: 5
    print(sol.maxValue([[1, 10, 100], [2, 5, 50], [6, 8, 20]], 2))  # Output: 150
    print(sol.maxValue([[1, 10, 100], [11, 20, 200]], 1))  # Output: 200
