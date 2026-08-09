class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import cache
        @cache
        def f(i, target):
            if i >= len(coins):
                return 1 if target == 0 else None
            k = 0
            ways = 0
            while target - k * coins[i] >= 0:
                w = f(i + 1, target - k * coins[i] )
                if w is not None:
                    ways += w
                k += 1
            return ways

        return f(0, amount )