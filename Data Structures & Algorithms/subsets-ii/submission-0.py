class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = [[]]
        for x in counter.keys():
            new_sub_sets = []
            for k in range(1, counter[x] + 1):
                for r in res:
                    new_sub_sets.append(r + [x] * k)
            res.extend(new_sub_sets)
        return res