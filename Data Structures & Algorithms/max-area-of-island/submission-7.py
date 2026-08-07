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
            if size[root_y] < size[root_x]:
                root_x, root_y = root_y, root_x
            parent[root_x] = root_y
            size[root_y] += size[root_x]
            return True
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    x = i * n + j
                    if i > 0 and grid[i - 1][j]:
                        union(x, x- n)
                    if j > 0 and grid[i][j - 1]:
                        union(x, x - 1)
                    maxSize = max(maxSize, size[find(x)])
        
 
        return maxSize


        