class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        hasOne = nums[0] == 1 
        if hasOne:
            nums = nums[1:]
        R = []
        #print(nums)
        for i in range(len(nums)):
            pick = nums[i]
            res = [pick]
            for j in range(i + 1, len(nums)):
                if nums[j] % pick == 0:
                    pick = nums[j]
                    res.append(pick)
            
            R.append(res)
        #print(R)
        ML = max(R, key = len)
        if hasOne:
            ML = [1] + ML
        return ML