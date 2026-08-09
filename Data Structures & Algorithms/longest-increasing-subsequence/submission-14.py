from sortedcontainers import SortedList
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

            # f(i, k) is the longest increasing Subsequence from [i -> end] given the previous element is last 
        dp = [1] * len(nums)

        r = 1
        for j in range(len(nums)):
            for i in range(j):
                if nums[i] < nums[j] and dp[i] >= dp[j]:
                    dp[j] = 1 + dp[i]
                    if dp[j] > r:
                        r = dp[j]
        return r