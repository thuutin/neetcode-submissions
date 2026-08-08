class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            i, j, d= q.popleft()
            if grid[i][j] > 0 and grid[i][j] <= d:
                continue
            grid[i][j] = d
            for di, dj in [(0, -1),(0, 1),(1, 0),(-1, 0)]:
                ni, nj = di + i, dj + j
                if ni < 0 or ni >=m or nj < 0 or nj >= n:
                    continue
                if grid[ni][nj] == -1:
                    continue
                if grid[ni][nj] <= d + 1:
                    continue
                q.append((ni, nj, d + 1))
        return None