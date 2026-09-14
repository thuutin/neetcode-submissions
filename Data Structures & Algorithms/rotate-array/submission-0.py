class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        k %= len(nums)
        i = -k
        while len(res) < len(nums):
            res.append(nums[i])
            i += 1
        for i in range(len(nums)):
            nums[i] = res[i]
        return None