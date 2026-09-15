class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums =  nums 
        from functools import cache
        def getItem(i):
            if i == -1:
                return 1
            if i >= len(nums):
                return 1
            return nums[i]
        @cache
        def dp(i, j):
            if i >= j:
                return getItem(i) * getItem(i - 1) * getItem(i + 1)
            max_coin = None
            for last in range(i, j + 1):
                burst = getItem(last) * getItem(i - 1) * getItem(j + 1)
                if last > i:
                    burst += dp(i, last - 1)
                if last < j:
                    burst += dp(last + 1, j)
                if max_coin == None or max_coin < burst:
                    max_coin = burst
            return max_coin

        return dp(0, len(nums) - 1)