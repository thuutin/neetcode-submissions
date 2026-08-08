class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((0, i,j))
        dirs = [(0, -1),(0, 1),(1, 0),(-1, 0)]
        while q:
            d, i, j = q.popleft()
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if ni < 0 or ni >=m or nj < 0 or nj >= n:
                    continue
                if grid[ni][nj] == -1:
                    continue
                if grid[ni][nj] <= d + 1:
                    continue
                grid[ni][nj] = d + 1
                q.append((d+1, ni, nj))

        return None