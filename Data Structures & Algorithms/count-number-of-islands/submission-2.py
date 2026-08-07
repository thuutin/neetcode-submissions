class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
                    visisted.add((ii, jj))
                    if grid[ii][jj] == '1':
                        q.append((ii, jj))

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' or (i, j) in visisted:
                    continue
                bfs(i, j)
                islands += 1
        return islands