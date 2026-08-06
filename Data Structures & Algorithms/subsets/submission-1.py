class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in nums:
            new = []
            for r in res:
                new.append(r + [x])
            res.extend(new)
        return res
