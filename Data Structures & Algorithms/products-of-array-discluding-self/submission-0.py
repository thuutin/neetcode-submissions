class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff = [1] * len(nums)
        suff[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = nums[i] * suff[i+1]
        res = [1] * len(nums)
        prev = 1
        for i in range(len(res)):
            res[i] = prev
            if i + 1 < len(suff):
                res[i] *= suff[i + 1]
            prev *= nums[i]
        return res
