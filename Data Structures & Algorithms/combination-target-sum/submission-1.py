class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [[]]
        for x in nums:
            new = []
            for r in res:
                s = sum(r)
                times = 1
                while s + x * times <= target:
                    new.append(r + [x] * times)
                    times += 1
            res.extend(new)
        return list(filter(lambda r: sum(r) == target, res))
