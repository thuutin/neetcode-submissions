class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [float("inf")] * len(nums)
        jumps[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                jumps[i] = min(jumps[j] + 1, jumps[i] )
        return jumps[0]