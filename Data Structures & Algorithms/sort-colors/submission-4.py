class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        target = 0
        i = 0
        while i < len(nums):
            if nums[i] == target:
                i += 1
                continue
            j = i + 1
            while j < len(nums) and nums[j] != target:
                j += 1
            if j >= len(nums):
                if target == 0:
                    target = 1
                    continue
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        