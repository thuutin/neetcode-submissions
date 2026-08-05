class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while start < end - 1 and nums[start] > nums[end]:
            mid = (start + end + 1) // 2
            if nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid
        return min(nums[start: end + 1])

