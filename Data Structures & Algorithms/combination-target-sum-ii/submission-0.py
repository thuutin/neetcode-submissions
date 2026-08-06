class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [[]]
        counter = Counter(candidates)
        for x in sorted(set(candidates)):
            new = []
            for r in res:
                s = sum(r)
                for times in range(1, counter[x] + 1):
                    if s + x * times <= target:
                        new.append(r + [x] * times)
            res.extend(new)
        return list(filter(lambda r: sum(r) == target, res))
