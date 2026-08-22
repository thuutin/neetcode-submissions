class Solution:
    def myPow(self, x: float, n: int, f = 1) -> float:
        if n == 1:
            return x * f
        if n == 0:
            return f
        if n < 0:
            return 1 / self.myPow(x, -n, f)
        if n%2 ==1:
            f *=x

        return self.myPow(x * x, n // 2, f)