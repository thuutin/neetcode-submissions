class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import cache
        @cache
        def dp(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            skip1 = dp(i + 1, j)
            skip2 = dp(i, j + 1)
            options =[ skip1, skip2]
            if text1[i] == text2[j]:
                take = 1 + dp(i + 1, j + 1)
                options.append(take)
            return max(options)

        return dp(0, 0)