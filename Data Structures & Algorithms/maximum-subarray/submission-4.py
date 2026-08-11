class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxS = nums[0]
        for x in nums:
            s = max(x, x + s)
            maxS = max(maxS, s)
        return maxS