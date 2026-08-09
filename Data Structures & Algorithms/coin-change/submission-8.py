class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[None] * len(coins) for _ in range(amount + 1)]
        for sub_amount in range(amount + 1):
            dp[sub_amount][0] = (sub_amount // coins[0]) if sub_amount % coins[0] == 0 else None
        for i in range(1, len(coins)):
            c = coins[i]
            for sub_amount in range(amount + 1):
                x = 0
                current = dp[sub_amount][i]
                while sub_amount - x * c >= 0:
                    xx = dp[sub_amount - x * c][i - 1]
                    if xx == None:
                        x += 1
                        continue
                    if not current:
                        current = xx + x
                    else:
                        current = min(current, xx + x)
                    x += 1
                dp[sub_amount][i] = current
        x = dp[amount][-1]
        return x if x is not None else -1