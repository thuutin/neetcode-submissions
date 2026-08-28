class Solution:
    def totalNQueens(self, n: int) -> int:
        def bt(col_set, diag, other_diag):
            if len(col_set) == n:
                return 1
            count = 0
            i = len(col_set)
            for j in range(n):
                if j in col_set or (i + j) in diag or (i - j) in other_diag:
                    continue
                col_set.add(j)
                diag.add(i + j)
                other_diag.add(i - j)
                count += bt(col_set, diag, other_diag)
                col_set.remove(j)
                diag.remove(i + j)
                other_diag.remove(i - j)
            return count
        return bt(set(), set(), set())