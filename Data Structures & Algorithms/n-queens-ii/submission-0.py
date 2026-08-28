class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def check(queen_cols):
            diag = set()
            other_diag = set()
            for i, j in enumerate(queen_cols):
                if i + j in diag:
                    return False
                if i - j in other_diag:
                    return False
                diag.add(i + j)
                other_diag.add(i - j)
            return True

        def bt(queen_cols, col_set):
            if len(queen_cols) == n:
                if check(queen_cols):
                    return 1
                return 0
            count = 0
            for j in range(n):
                if j in col_set:
                    continue
                queen_cols.append(j)
                col_set.add(j)
                count += bt(queen_cols, col_set)
                col_set.remove(j)
                queen_cols.pop()
            return count
        return bt([], set())