class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        maxSoFar = dp[0]
        for i in range(2, len(nums)):
            dp[i] = maxSoFar + nums[i]
            maxSoFar = max(maxSoFar, dp[i - 1])
        return max(dp)