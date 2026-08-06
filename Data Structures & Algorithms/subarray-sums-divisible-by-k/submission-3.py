class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [0] * k
        count[0] = 1
        prefix = res = 0

        for num in nums:
            prefix = (prefix + num + k) % k
            res += count[prefix]
            count[prefix] += 1

        return res