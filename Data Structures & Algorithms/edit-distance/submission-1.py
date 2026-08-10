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
        return f(0, 0)