class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    match_cost = dp[i - 1][j - 1]
                    change_cost = dp[i - 1][j - 1] + 1
                    add_cost = dp[i][j - 1] + 1
                    delete_cost = dp[i - 1][j] + 1
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = min(add_cost, delete_cost, match_cost)
                    else:
                        dp[i][j] = min(add_cost, delete_cost, change_cost)

        return dp[-1][-1]