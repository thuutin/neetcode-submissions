class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from functools import cache
        @cache
        def dp(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            select = dp(i + 1, j + 1) if s[i] == t[j] else 0 
            skip = dp(i + 1, j)
            return select + skip
        return dp(0, 0)
