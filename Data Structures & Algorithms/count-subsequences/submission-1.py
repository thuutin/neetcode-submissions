class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(len(t), -1, -1):
                if j == len(t):
                    dp[i][j] = 1
                    continue
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]                
                dp[i][j] += dp[i + 1][j]
        for r in dp:
            print(r)
        return dp[0][0]