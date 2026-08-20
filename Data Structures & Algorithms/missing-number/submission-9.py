class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for x in nums:
            xor ^= x
        for x in range(1, len(nums) + 1):
            xor ^= x
        return xor
        