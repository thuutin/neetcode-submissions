class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [(newInterval[0], newInterval[1])]
        for s1, e1 in intervals:
            (s2, e2) = res.pop()
            if s2 < s1:
                s1, e1, s2, e2 = s2, e2, s1, e1
            if s2 <= e1:
                res.append( (min(s1, s2), max(e1, e2)) )
            else:
                res.extend([(s1, e1), (s2, e2)])
        return res
