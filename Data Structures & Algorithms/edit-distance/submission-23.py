class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = list(range(len(word2) + 1))
        dp = [0] * (len(word2) + 1)
        for i in range(1, len(word1) + 1):
            dp[0] = i
            for j in range(1, len(word2) + 1):
                match_cost = prev[j - 1] if word1[i-1] == word2[j-1] else prev[j - 1]  + 1
                add_cost = dp[j - 1] + 1
                delete_cost = prev[j] + 1
                dp[j] = min(add_cost, delete_cost, match_cost)

            prev, dp = dp, prev
            
        return prev[-1]