class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 != 0:
            return False
        HALF = S // 2
        from functools import cache
        @cache
        def f(i, s1, s2):
            if i >= len(nums):
                return s1 == s2
            if s1 > HALF or s2 > HALF:
                return False
            r = f(i + 1, s1 + nums[i], s2) or f(i + 1, s1, s2 + nums[i])
            return r
        return f(0, 0,0)