class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        reachable = [(0, tuple(points[0]))]
        visited = set()
        cost = 0
        while len(visited) < len(points):
            dd, (x, y) = heapq.heappop(reachable)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            cost += dd
            for x1, y1 in points:
                if (x1, y1) not in visited:
                    d = abs(x1 - x) + abs(y1 - y)
                    heapq.heappush(reachable, (d, (x1, y1)))
        return cost