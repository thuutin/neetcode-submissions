class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mods = [[0] * k for _ in range(len(nums))]
        s = 0
        for i, x in enumerate(nums):
            for m in range(0, k):
                if i > 0:
                    mods[i][m] = mods[i - 1][(m-x) % k]
            mods[i][x%k] += 1
        
            s += mods[i][0]
        return s