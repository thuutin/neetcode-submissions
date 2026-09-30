class Solution:
    def totalNQueens(self, n: int) -> int:
        c = 0
        def check(qs):
            #print(qs)
            dia = set()
            cross = set()
            for i, j in enumerate(qs):
                ss = i + j
                st = i - j
                if ss in dia:
                    return False
                if st in cross:
                    return False
                dia.add(ss)
                cross.add(st)
            return True
        def dfs(qs, s):
            nonlocal c
            if len(qs) == n:
                if check(qs):
                    c += 1
                return None
                
            for j in range(n):
                if j not in s:
                    qs.append(j)
                    s.add(j)
                    dfs(qs, s)
                    s.remove(j)
                    qs.pop()
        dfs([], set())
        return c
        



