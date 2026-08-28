class Solution:
    def totalNQueens(self, n: int) -> int:
        def bt(i, col_set, diag, other_diag):
            if i == n:
                return 1
            count = 0
            for j in range(n):
                if j in col_set or (i + j) in diag or (i - j) in other_diag:
                    continue
                col_set.add(j)
                diag.add(i + j)
                other_diag.add(i - j)
                count += bt(i + 1, col_set, diag, other_diag)
                col_set.remove(j)
                diag.remove(i + j)
                other_diag.remove(i - j)
            return count
        return bt(0, set(), set(), set())