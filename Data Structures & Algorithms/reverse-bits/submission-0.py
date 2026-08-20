class Solution:
    def reverseBits(self, n: int) -> int:
        r = []
        for i in range(32):
            if (n >> i) & 1 == 1:
                r.append(1)
            else:
                r.append(0)
        res = 0
        for bit in r:
            if bit:
                res *= 2
                res += 1
            else:
                res *= 2
        return res