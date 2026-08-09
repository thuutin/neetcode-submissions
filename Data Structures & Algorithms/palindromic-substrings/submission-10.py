class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(set(s)) == 1:
            x = len(s)
            s = 0
            while x > 0:
                s += x
                x -= 1
            return s
        dp = {}
        c = len(s)
        for size in range(2, len(s) + 1):
            i = 0
            maxI = len(s) - size + 1
            while i < maxI:
                j = i + size - 1
                ok = s[i] == s[j]
                if size > 3:
                    ok = ok and dp[(i+1, j - 1)]
                if ok:
                    c += 1
                dp[(i,j)] = ok
                i += 1
        return c