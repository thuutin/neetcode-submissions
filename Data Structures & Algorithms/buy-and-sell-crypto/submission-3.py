class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        maxP = 0
        for i in range(1, len(prices)):
            x = prices[i]
            maxP = max(maxP, x - minSoFar)
            minSoFar = min(minSoFar, x)
        return maxP