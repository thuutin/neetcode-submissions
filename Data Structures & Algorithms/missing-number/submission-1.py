class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        for x in range(1, n + 1):
            s += x
        return s - sum(nums)