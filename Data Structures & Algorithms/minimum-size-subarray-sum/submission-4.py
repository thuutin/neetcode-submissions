class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        s = 0
        minL = None
        while j < len(nums):
            s += nums[j]
            j += 1
            while s >= target:
                if minL is None or minL > j - i:
                    minL = j - i
                s -= nums[i]
                i += 1
        if minL == None:
            return 0
        return minL