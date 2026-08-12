"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        maxSize = 0
        for interval in sorted(intervals, key = lambda x: x.start):
            start, end = interval.start, interval.end
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
            maxSize = max(len(rooms), maxSize)

        return maxSize