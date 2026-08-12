"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = defaultdict(int)
        ends = defaultdict(int)
        events = set()
        for i in range(len(intervals)):
            starts[intervals[i].start] += 1
            ends[intervals[i].end] += 1
        events.update(starts.keys())
        events.update(ends.keys())
        rooms = 0
        maxRooms = 0
        for e in sorted(events):
            rooms += starts[e] - ends[e]
            maxRooms = max(maxRooms, rooms)
        return maxRooms