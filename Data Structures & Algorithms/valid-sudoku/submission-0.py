class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        def insert_if_no_duplicate(prev, x):
            if x in prev:
                return False
            prev.add(x)
            return True

        for i in range(len(board)):
            for j in range(len(board[i])):
                square_index = i // 3 * 3 + j // 3
                sets = [squares[square_index], rows[i], cols[j]]
                x = board[i][j]
                if x == '.':
                    continue
                for s in sets:
                    if not insert_if_no_duplicate(s, x):
                        return False
        return True