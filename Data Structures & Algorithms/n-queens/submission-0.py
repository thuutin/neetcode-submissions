class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(queens, i , j):
            for qi, qj in queens:
                if qj == j:
                    return False
                if qi + qj == i + j or qi - qj == i - j:
                    return False
            return True
        res = []
        def generate(queens):
            board = []
            for i in range(n):
                row = ""
                qj = queens[i][1]
                for j in range(n):
                    if qj == j:
                        row += "Q"
                    else:
                        row += "."
                board.append(row)
            return board

        def backtrack(i, queens):
            if i >= n:
                res.append(generate(queens))
            for j in range(n):
                if valid(queens, i, j):
                    queens.append((i, j))
                    backtrack(i + 1, queens)
                    queens.pop()
                
        backtrack(0, [])
        return res