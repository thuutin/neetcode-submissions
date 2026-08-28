class Solution:
    def totalNQueens(self, n: int) -> int:
        def bt(queen_cols, col_set, diag, other_diag):
            if len(queen_cols) == n:
                return 1
            count = 0
            i = len(queen_cols)
            for j in range(n):
                if j in col_set or (i + j) in diag or (i - j) in other_diag:
                    continue
                queen_cols.append(j)
                col_set.add(j)
                diag.add(i + j)
                other_diag.add(i - j)
                count += bt(queen_cols, col_set, diag, other_diag)
                col_set.remove(j)
                queen_cols.pop()
                diag.remove(i + j)
                other_diag.remove(i - j)
            return count
        return bt([], set(), set(), set())