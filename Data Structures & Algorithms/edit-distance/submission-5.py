class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = None
        for i in range(len(word1) + 1):
            dp = [0] * (len(word2) + 1)
            for j in range(len(word2) + 1):
                if i == 0:
                    dp[j] = j
                elif j == 0:
                    dp[j] = i
                else:
                    match_cost = prev[j - 1]
                    change_cost = prev[j - 1] + 1
                    add_cost = dp[j - 1] + 1
                    delete_cost = prev[j] + 1
                    if word1[i-1] == word2[j-1]:
                        dp[j] = min(add_cost, delete_cost, match_cost)
                    else:
                        dp[j] = min(add_cost, delete_cost, change_cost)
            prev = dp
        return dp[-1]