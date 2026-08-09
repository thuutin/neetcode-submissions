class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from functools import cache
        @cache
        def f(i, last):
            # f(i, k) is the longest increasing Subsequence from [i -> end] given the previous element is last 
            if i >= len(nums):
                return 0
            skip = f(i + 1, last)
            options = [skip]
            if last is None or nums[i] > last:
                take = 1 + f(i + 1, nums[i])
                options.append(take)
            return max(options)
        return f(0, None)