class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        import bisect
        intervals.sort(key=lambda x:x[0])
        #print(intervals)
        starts = []
        for s, _ in intervals:
            starts.append(s)
        from functools import cache
        @cache
        def dp(i):
            if i >= len(intervals):
                return 0
            s, e = intervals[i]
            j = bisect.bisect_left(starts, e, lo=i + 1)
            keep = j - i - 1 + dp(j)
            drop = 1 + dp(i + 1)
            return min(keep, drop)
        
        return dp(0)
