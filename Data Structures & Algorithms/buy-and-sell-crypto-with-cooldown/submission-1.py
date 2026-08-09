class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache
        @cache
        def dp(i, bought):
            if i >= len(prices):
                return 0
            skip = dp(i + 1, bought)
            if not bought:
                buy = - prices[i] + dp(i + 1, True)
                return max(buy, skip)
            else:
                sell = prices[i] + dp(i + 2, False)
                return max(skip, sell)
        return dp(0, False)