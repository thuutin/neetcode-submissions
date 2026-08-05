class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            c = 0
            for i in range(len(nums)):
                if nums[i] <= mid and nums[i] >= start:
                    c += 1
            if c > mid - start + 1:
                end = mid
            else:
                start = mid + 1
        return start
            
            