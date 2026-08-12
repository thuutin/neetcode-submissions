class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache
        @cache
        def dp(i, canbuy):
            if i >= len(prices):
                return 0
            prof = [dp(i + 1, canbuy)]
            if canbuy:
                buy = - prices[i] + dp(i + 1, False)
                prof.append(buy)
            else:
                sell = prices[i] + dp(i + 1, True)
                prof.append(sell)
            return max(prof)

        return dp(0, True)