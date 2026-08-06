class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mods = [[0] * k for _ in range(len(nums))]
        prev = [0] * k
        curr = [0] * k
        s = 0
        for i, x in enumerate(nums):
            for m in range(0, k):
                curr[m] = prev[(m-x) % k]
            curr[x%k] += 1
            s += curr[0]
            prev, curr = curr, prev

        return s