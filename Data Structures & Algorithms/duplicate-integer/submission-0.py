class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        H = set()
        for x in nums:
            if x in H:
                return True
            H.add(x)
        return False