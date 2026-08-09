class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1] * len(coins) for _ in range(amount + 1)]
        for sub_amount in range(0, amount + 1):
            dp[sub_amount][0] = (sub_amount // coins[0]) if sub_amount % coins[0] == 0 else -1
        for i in range(1, len(coins)):
            c = coins[i]
            for sub_amount in range(amount + 1):
                x = 0
                choices = []
                while sub_amount - x * c >= 0:
                    xx = dp[sub_amount - x * c][i - 1]
                    if xx != -1:
                        choices.append(xx + x)
                    x += 1
                if len(choices) > 0:
                    dp[sub_amount][i] = min(choices)
        return dp[amount][-1]