class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #queries = [(q, i) for i, q in enumerate(queries)]
        #queries.sort(key = lambda x: x[0])
        intervals.sort(key = lambda x: x[0])
        i = 0
        res = {}
        openings = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(openings, (size, intervals[i][1]))
                i += 1
            while openings and openings[0][1] < q:
                heapq.heappop(openings)
            res[q] = openings[0][0] if openings else -1
        return [res[q] for q in queries]