from typing import List
from heapq import heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        booked, free, res = [], list(range(n)), [0] * n
        meetings.sort()

        for start, end in meetings:
            while booked and booked[0][0] <= start:
                _, room = heappop(booked)
                heappush(free, room)

            if free:
                room = heappop(free)
                heappush(booked, (end, room))
            else:
                release, room = heappop(booked)
                heappush(booked, (release + (end - start), room))

            res[room] += 1

        return res.index(max(res))


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.mostBooked(2, [[0, 10], [1, 2], [2, 3], [3, 4]]))  # Example test case
    print(sol.mostBooked(3, [[0, 5], [1, 2], [2, 3], [3, 4]]))  # Example test case
    print(sol.mostBooked(1, [[0, 10], [5, 15]]))  # Example test case
    print(sol.mostBooked(4, [[0, 10], [5, 15], [10, 20]]))  # Example test case
