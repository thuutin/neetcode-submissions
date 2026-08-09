class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for xx in nums:
            x ^= xx
        return x