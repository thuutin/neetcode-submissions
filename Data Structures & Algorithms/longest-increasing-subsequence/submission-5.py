class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

            # f(i, k) is the longest increasing Subsequence from [i -> end] given the previous element is last 
        dp = [1] * len(nums)
        for j in range(len(nums)):
            for i in range(j):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], 1 + dp[i])
        return max(dp)