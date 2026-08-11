class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        pending = 0
        maxS = 0
        for x in nums:
            pending += x
            if s + pending <= 0:
                pending = 0
                s = 0
            if pending > 0:
                s += pending
                pending = 0
            maxS = max(maxS, s)
        if max(nums) < 0:
            return max(nums)
        return maxS