class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        s = sum(range(1, n + 1))
        
        return s - sum(nums)