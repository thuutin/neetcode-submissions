class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rot = deque([])
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rot.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh.add((i, j))
        L = 0
        V = set()
        while rot:
            #print(rot)
            if not fresh:
                break
            i, j, level = rot.popleft()
            fresh.discard((i, j))
            if (i, j) in V:
                continue
            L = max(L, level)
            V.add((i, j))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ii = di + i
                jj = dj + j
                if ii < 0 or ii >= m:
                    continue
                if jj < 0 or jj >= n:
                    continue
                if grid[ii][jj] == 0:
                    continue
                rot.append((ii, jj, level + 1))
        if fresh:
            return -1
        return L