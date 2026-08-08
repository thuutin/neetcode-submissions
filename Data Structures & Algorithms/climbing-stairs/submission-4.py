class Solution:
    def climbStairs(self, n: int) -> int:
        t1 = 1
        t2 = 1
        for i in range(2, n + 1):
            t1, t2 = t2, t1 + t2
        return t2
        