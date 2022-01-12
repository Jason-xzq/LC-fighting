class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] >= free_rooms[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, interval[1])
        return len(free_rooms)
