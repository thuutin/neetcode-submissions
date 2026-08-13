class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort(key = lambda x: x[0])
        intervals.sort(key = lambda x: x[0])
        i = 0
        res = [-1] * len(queries)
        openings = []
        for q, index in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(openings, (size, intervals[i][1]))
                i += 1
            while openings and openings[0][1] < q:
                heapq.heappop(openings)
            if openings:
                res[index] = openings[0][0]
        return res

            