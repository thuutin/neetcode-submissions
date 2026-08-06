class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            new = []
            for r in res:
                for x in nums:
                    if x not in r:
                        new.append(r + [x])
            res = new
        return res