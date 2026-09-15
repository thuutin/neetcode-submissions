class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        from functools import cache
        @cache
        def dp(i, j):
            if i >= j:

                return nums[i] * nums[i - 1] * nums[i + 1]
            max_coin = None
            for last in reversed(range(i, j + 1)):
                burst = nums[last] * nums[i - 1] * nums[j + 1]
                if last > i:
                    burst += dp(i, last - 1)
                if last < j:
                    burst += dp(last + 1, j)
                if max_coin == None or max_coin < burst:
                    max_coin = burst
            return max_coin

        return dp(1, len(nums) - 2)