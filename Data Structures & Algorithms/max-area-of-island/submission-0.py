class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visisted = set()
        def bfs(i, j):
            q = deque([(i,j)])
            visisted.add((i, j))
            while q:
                i, j = q.popleft()
                
                for di, dj in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
                    ii, jj = di + i, dj + j
                    if ii < 0 or ii >= len(grid):
                        continue
                    if jj < 0 or jj >= len(grid[i]):
                        continue
                    if (ii, jj) in visisted:
                        continue
                    if grid[ii][jj] == 1:
                        visisted.add((ii, jj))
                        q.append((ii, jj))

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i, j) in visisted:
                    continue
                before = len(visisted)
                bfs(i, j)
                islands = max(islands, len(visisted) - before)
        return islands

        