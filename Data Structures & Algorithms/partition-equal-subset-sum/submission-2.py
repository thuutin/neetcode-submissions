class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 != 0:
            return False
        HALF = S // 2
        cache = {}
        def f(i, s1, s2):
            if i >= len(nums):
                return s1 == s2
            if s1 > HALF or s2 > HALF:
                return False
            k = i, s1, s2
            if k in cache:
                return cache[k]
            r = f(i + 1, s1 + nums[i], s2) or f(i + 1, s1, s2 + nums[i])
            cache[k] = r
            return r
        return f(0, 0,0)