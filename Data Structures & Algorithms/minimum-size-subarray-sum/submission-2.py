class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        s = 0
        minL = float("inf")
        while j < len(nums):
            s += nums[j]
            j += 1
            while s >= target:
                minL = min(minL, j - i)
                s -= nums[i]
                i += 1
        if minL == float("inf"):
            return 0
        return minL