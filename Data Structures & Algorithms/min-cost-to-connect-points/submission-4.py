class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nextPoint = points[0]
        visited = set()
        cost = 0
        D = defaultdict(lambda : float("inf"))
        D[tuple(nextPoint)] = 0
        while nextPoint:
            (x, y) = nextPoint
            if (x, y) in visited:
                continue
            visited.add((x, y))
            cost += D[(x, y)]
            nextPoint = None
            for x1, y1 in points:
                if (x1, y1) in visited:
                    continue
                d = abs(x1 - x) + abs(y1 - y)
                D[(x1, y1)] = min(d, D[(x1, y1)])
                if nextPoint == None or D[nextPoint] > D[(x1, y1)]:
                    nextPoint = (x1, y1)
        return cost