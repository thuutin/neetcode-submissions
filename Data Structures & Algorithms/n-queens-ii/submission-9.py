class Solution:
    def totalNQueens(self, n: int) -> int:
        c = 0
        def dfs(qs, s, cross, dia):
            nonlocal c
            if len(qs) == n:
                c += 1
                return None
            i = len(qs)
            for j in range(n):
                if j in s or (i + j) in cross or (i - j) in dia:
                    continue
                qs.append(j)
                s.add(j)
                cross.add(i + j)
                dia.add(i - j)
                dfs(qs, s, cross, dia)
                s.remove(j)
                qs.pop()
                cross.remove(i + j)
                dia.remove(i - j)
        dfs([], set(), set(), set())
        return c
        



