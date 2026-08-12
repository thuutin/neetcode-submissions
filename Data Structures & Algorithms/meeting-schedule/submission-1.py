"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                s1, e1 = intervals[i].start, intervals[i].end 
                s2, e2 = intervals[j].start, intervals[j].end
                if s2 < s1:
                    s1, e1, s2, e2 = s2, e2, s1, e1
                if s2 < e1:
                    return False
        return True