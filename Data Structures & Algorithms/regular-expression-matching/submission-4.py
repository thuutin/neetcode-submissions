class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        stars = []
        for i, c in enumerate(p):
            if c == '*':
                stars.append(p[i - 1])
        pp = []
        for i, c in enumerate(p):
            if c == '.' and (i >= len(p) - 1 or p[i + 1] != '*'):
                pp.append(c)
            elif c == '*':
                continue
            else:
                if i < len(p) - 1 and p[i + 1] == '*':
                    pp.append('*')
                else:
                    pp.append(c)
        j = 0
        st = {}
        for i, c in enumerate(pp):
            if c == '*':
                st[i] = stars[j]
                j += 1
        p = "".join(pp)
        print(p)
        from functools import cache
        print(st)
        @cache
        def solve(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if i >= len(s):
                t = p[j:]
                for c in t:
                    if c != '*':
                        return False

                return True
            if j >= len(p):
                return False
            print(i, j)

            if p[j] not in '*.' and s[i] == p[j]:
                return solve( i + 1, j + 1)
            elif p[j] == '.':
                return solve(i + 1, j + 1)
            elif p[j] == '*':
                if st[j] == '.':
                    return solve(i + 1, j) or solve(i, j + 1)
                elif st[j] == s[i]:
                    return solve(i + 1, j) or solve(i, j + 1)
                else:
                    return solve(i, j + 1)
            else:
                return False

        return solve(0, 0)