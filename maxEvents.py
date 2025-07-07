import heapq


class Solution(object):
    def maxEvents(self, events):
        events = sorted(events, key=lambda x: x[0])  # 1
        total_days = max(event[1] for event in events)  # 2
        min_heap = []  # 3
        day, cnt, event_id = 1, 0, 0  # 4

        while day <= total_days:  # 5
            # if no events are available to attend today, let time flies to the next available event.
            if event_id < len(events) and not min_heap:  # 6
                day = events[event_id][0]  # 7

            # all events starting from today are newly available. add them to the heap.
            while event_id < len(events) and events[event_id][0] <= day:  # 8
                heapq.heappush(min_heap, events[event_id][1])  # 9
                event_id += 1  # 10

            # if the event at heap top already ended, then discard it.
            while min_heap and min_heap[0] < day:  # 11
                heapq.heappop(min_heap)  # 12

            # attend the event that will end the earliest
            if min_heap:  # 13
                heapq.heappop(min_heap)  # 14
                cnt += 1  # 15
            elif event_id >= len(events):  # 16
                break  # no more events to attend. so stop early to save time.
            day += 1  # 17
        return cnt  # 18


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxEvents([[1, 2], [2, 3], [3, 4]]))  # Output: 3
    print(sol.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]))  # Output: 4
    print(sol.maxEvents([[1, 100000]]))  # Output: 1
    print(sol.maxEvents([[1, 2], [2, 3], [3, 4], [4, 5]]))  # Output: 4
