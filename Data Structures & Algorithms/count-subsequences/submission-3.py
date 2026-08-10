class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t)) for _ in range(len(s))]
        dp[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    if i > 0 and j > 0:
                        dp[i][j] += dp[i-1][j-1]
                    else:
                        dp[i][j] += 1
                dp[i][j] += dp[i - 1][j]
        for r in dp:
            print(r)
        return dp[-1][-1]