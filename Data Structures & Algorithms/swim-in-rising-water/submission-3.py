class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = [(grid[0][0] ,0, 0)]
        water_levels = defaultdict(lambda : float("inf"))
        water_levels[(0, 0)] = grid[0][0]
        m = len(grid)
        n = len(grid[0])
        diff = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        while pq:
            level, i, j = heapq.heappop(pq)
            if level > water_levels[(i, j)]:
                continue
            if (i, j) == (m - 1, n - 1):
                return level
            for di, dj in diff:
                ni = i + di
                nj = j + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                new_level = max(grid[ni][nj], level)
                if water_levels[(ni, nj)] > new_level:
                    water_levels[(ni, nj)] = new_level
                    heapq.heappush(pq, (new_level, ni, nj))
        
        return water_levels[(m - 1, n - 1)]