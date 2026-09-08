class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        for k in list(c.keys()):
            if c[k] <= len(nums) //3:
                del c[k]
        return list(c.keys())