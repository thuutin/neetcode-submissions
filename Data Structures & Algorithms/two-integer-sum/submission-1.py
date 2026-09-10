class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}
        for i, x in enumerate(nums):
            complement = target -x 
            if complement in H:
                return [H[complement], i]
            H[x] = i
        return None
