class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from functools import cache
        @cache
        def f(i, j):
            if j >= len(word2):
                return len(word1) - i
            if i >= len(word1):
                return len(word2) - j
            minCost = 1 + min(f(i, j + 1), f(i + 1, j)) 
            cost = f(i + 1, j + 1)
            if word1[i] == word2[j]:
                minCost = min(minCost, cost)
            else:
                minCost = min(minCost, cost + 1)
            return minCost

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