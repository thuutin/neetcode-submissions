class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        import bisect
        intervals.sort(key=lambda x:x[0])
        from functools import cache
        @cache
        def dp(i):
            if i >= len(intervals):
                return 0
            s, e = intervals[i]
            j = bisect.bisect_left(intervals, [e, 0], lo = i + 1)
            rm = j - i - 1
            keep = rm + dp(j)
            if rm <= 1:
                return keep
            drop = 1 + dp(i + 1)
            return min(keep, drop)
        
        return dp(0)
