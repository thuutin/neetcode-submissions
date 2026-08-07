class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        parent = [i for i in range(m * n)]
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return x
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            parent[root_y] = root_x
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    x = i * n + j
                    for di, dj in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
                        ii, jj = di + i, dj + j
                        if ii < 0 or ii >= len(grid):
                            continue
                        if jj < 0 or jj >= len(grid[i]):
                            continue
                        if grid[ii][jj] == '1':
                            y = ii * n + jj
                            union(x, y)
        #print(parent)
        pSet = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    #print(i*n+j, find(i*n+j))
                    pSet.add(find(i*n+j))
        #print(pSet)
        return len(pSet)
