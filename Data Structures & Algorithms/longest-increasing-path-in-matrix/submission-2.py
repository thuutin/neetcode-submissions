class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        DOWN = [ [1] * n for _ in range(m) ]
        UP = [ [1] * n for _ in range(m) ]
        LEFT = [ [1] * n for _ in range(m) ]
        RIGHT = [ [1] * n for _ in range(m) ]
        done = set()
        def fill(i, j, which):
            k = i, j, which
            if k in done:
                return None
            that = None
            if which == 0:
                ni, nj = i + 1, j
                that = DOWN
            elif which == 1:
                ni, nj = i - 1, j
                that = UP
            elif which == 2:
                ni, nj = i, j - 1
                that = LEFT
            else:
                ni, nj = i, j + 1
                that = RIGHT
            if ni < 0 or ni >= m or nj < 0 or nj >= n:
                that[i][j] = 1
            elif matrix[ni][nj] <= matrix[i][j]:
                that[i][j] = 1
            else:
                fill(ni, nj, 0)
                fill(ni, nj, 1)
                fill(ni, nj, 2)
                fill(ni, nj, 3)
                that[i][j] = 1 + max(DOWN[ni][nj], UP[ni][nj], LEFT[ni][nj], RIGHT[ni][nj])
            done.add(k)
            
        for i in range(m):
            for j in range(n):
                for w in [0, 1, 2, 3]:
                    fill(i, j, w)
        M = 0
        for i in range(m):
            for j in range(n):
                for w in [DOWN, UP, LEFT, RIGHT]:
                    M = max(M, w[i][j])
        return M
