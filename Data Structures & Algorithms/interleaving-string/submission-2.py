class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        from functools import cache
        @cache
        def f(i, j, diff):
            k = i + j
            if i >= len(s1) and j >= len(s2):
                return k >= len(s3) and abs(diff) <= 1
            if k >= len(s3):
                return False
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = res or f(i + 1, j, diff + 1)
            if j < len(s2) and s2[j] == s3[k]:
                res = res or f(i, j + 1, diff - 1)
            return res
        return f(0, 0, 0)