class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}
        for i, x in enumerate(nums):
            if (target -x) in H:
                return [H[target-x], i]
            H[x] = i
        return None
