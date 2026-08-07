class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = [i for i in range(m * n)]
        size = [1] * (m * n)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            parent[root_y] = root_x

            size[root_x] += size[root_y]
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x = i * n + j
                    if i > 0 and grid[i - 1][j]:
                        union(x, x- n)
                    if j > 0 and grid[i][j - 1]:
                        union(x, x - 1)
                    
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxSize = max(maxSize, size[find(i*n+j)])

        return maxSize


        