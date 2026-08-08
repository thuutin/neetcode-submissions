class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = []
        atlantic = []
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific.append((i, j))
                if i == m - 1 or j == n - 1:
                    atlantic.append((i, j))
        DIRS = [(0, 1),(0, -1),(1, 0), (-1, 0),]
        def bfs(source):
            flowable = set(source)
            q = deque(source)
            while q:
                i, j = q.popleft()
                for di, dj in DIRS:
                    ni, nj = di + i, dj + j
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        continue
                    if (ni, nj) in flowable:
                        continue
                    if heights[ni][nj] < heights[i][j]:
                        continue
                    flowable.add((ni, nj))
                    q.append((ni, nj))
            return flowable
            
        flowable_to_atlantic = bfs(atlantic)
        res = []
        for cell in bfs(pacific):
            if cell in flowable_to_atlantic:
                res.append(cell)
        return res
