class Solution:
    def countBits(self, n: int) -> List[int]:
        o = []
        for i in range(n + 1):
            o.append(Counter(bin(i))['1'])
        return o