class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        step = 0
        while r < len(nums) - 1:
            max_reachable = r
            for i in range(l, r + 1):
                max_reachable = max(max_reachable, i + nums[i])
            l, r = r + 1, max_reachable
            step += 1
        return step
            