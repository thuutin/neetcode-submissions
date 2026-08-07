class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(queens, i , j):
            for qi, qj in enumerate(queens):
                if qj == j:
                    return False
                if qi + qj == i + j or qi - qj == i - j:
                    return False
            return True
        res = []
        def generate(queens):
            board = [None] * n
            for i in range(n):
                qj = queens[i]
                row = "." * qj + "Q" + "." * (n - qj - 1)
                board[i] = row
            return board

        def backtrack(i, queens):
            if i >= n:
                res.append(generate(queens))
            for j in range(n):
                if valid(queens, i, j):
                    queens.append(j)
                    backtrack(i + 1, queens)
                    queens.pop()
                
        backtrack(0, [])
        return res