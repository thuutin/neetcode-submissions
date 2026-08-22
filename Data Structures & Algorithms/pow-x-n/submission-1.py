class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        f = 1
        if n % 2 == 1:
            f = x
        return f * self.myPow(x * x, n // 2)