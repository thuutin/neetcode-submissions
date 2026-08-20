class Solution:
    def reverse(self, x: int) -> int:
        xx = int(str(abs(x))[::-1])
        if x >= 0:
            x = xx
        else:
            x = -xx

        if x < -2 ** 31 or x > ( 2 ** 31 + 1):
            return 0
        return x