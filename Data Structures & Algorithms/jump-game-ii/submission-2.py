class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        step = 0
        while r < len(nums) - 1:
            rr = r

            for i in range(l, r + 1):
                rr = max(rr, i + nums[i])
            l, r = r + 1, rr
            step += 1
        return step
                
        # [2,2,1,1,1,1]
        # [3,3,2,2,1,0]
        # [0,1,1,2,3,4]