class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rot = deque([])
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rot.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        L = 0
        while rot:
            #print(rot)
            if not fresh:
                break
            for r in range(len(rot)):
                i, j = rot.popleft()
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ii = di + i
                    jj = dj + j
                    if ii < 0 or ii >= m:
                        continue
                    if jj < 0 or jj >= n:
                        continue
                    if grid[ii][jj] == 0 or grid[ii][jj] == 2:
                        continue
                    grid[ii][jj] = 2
                    fresh -= 1
                    rot.append((ii, jj))
            L += 1
        if fresh:
            return -1
        return L