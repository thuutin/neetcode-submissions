from sortedcontainers import SortedList
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

            # f(i, k) is the longest increasing Subsequence from [i -> end] given the previous element is last 
        dp = [1] * len(nums)

        r = 1
        left = SortedList()
        for j in range(len(nums)):
            i = left.bisect_left((nums[j], 0))
            #print(j, left, i)
            while i >= 0:
                if i < len(left) and left[i][0] < nums[j] and dp[left[i][1]] >= dp[j]:
                    dp[j] = 1 + dp[left[i][1]]
                    if dp[j] > r:
                        r = dp[j]
                i -= 1
            left.add((nums[j], j))
        return r