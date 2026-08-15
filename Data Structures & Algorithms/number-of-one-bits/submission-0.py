class Solution:
    def hammingWeight(self, n: int) -> int:
        c = Counter(bin(n))
        return c['1']