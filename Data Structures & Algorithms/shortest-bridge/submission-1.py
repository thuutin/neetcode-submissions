class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        source = set()
        des = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(node, where):
            i, j = node
            if i < 0 or i >= m or j < 0 or j >= n:
                return None
            if (i, j) in where:
                return None
            if grid[i][j] == 0:
                return None
            where.add((i ,j))
            dfs( (i + 1, j), where)
            dfs( (i - 1, j), where)
            dfs( (i , j - 1), where)
            dfs( (i , j + 1), where)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if (i, j) in source or (i, j) in des:
                    continue
                if len(source) == 0:
                    dfs((i, j), source)
                else:
                    dfs( (i, j), des)

        q = deque()
        V = set()
        for i, j in source:
            q.append((i, j, 0))
            V.add((i, j))
        while q:
            i, j, step = q.popleft()
            if (i, j) in des:
                return step - 1
            for di, dj in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
                ni, nj = di + i, dj + j
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if (ni, nj) in V:
                    continue
                V.add((ni, nj))
                q.append(( ni, nj, step + 1))
        return -1