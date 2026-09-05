class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        used = 0
        maxLength = 0
        while j < len(nums):
            if nums[j] == 1 or used < k:
                if nums[j] == 0:
                    used += 1
                j += 1
                maxLength = max(maxLength, j - i)
            else:
                if nums[i] == 0:
                    used -= 1
                i += 1
        return maxLength