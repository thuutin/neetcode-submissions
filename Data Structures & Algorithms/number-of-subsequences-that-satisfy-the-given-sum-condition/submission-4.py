class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for x in nums:
            if x * 2 <= target:
                res += 1
        #print(res)
        i = 0
        j = len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
                continue
            between = j - i
            w = pow(2, between, 10 ** 9 + 7) - 1
            res += w
            res = res % (10 ** 9 + 7)
            #print(i, j, w)
            i += 1
        return res