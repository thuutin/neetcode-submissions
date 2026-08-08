class Solution:
    def solve(self, board: List[List[str]]) -> None:
        O_on_edges = []
        O = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        O_on_edges.append((i, j))
                    O.append((i, j))

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
                    if board[ni][nj] == 'X':
                        continue
                    flowable.add((ni, nj))
                    q.append((ni, nj))
            return flowable
        strong_O = bfs(O_on_edges)

        for i, j in O:
            if (i, j) not in strong_O:
                board[i][j] = 'X'

        return None
