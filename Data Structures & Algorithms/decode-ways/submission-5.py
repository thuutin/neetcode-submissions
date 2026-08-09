class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        # dp[i] = dp[i - 1]
        # dp[i] += dp[i - 2] #if s[i - 1:i + 1] is 10 -> 26
        dp[0] = 1 if int(s[0]) > 0 else 0
        for i in range(1, len(s)):
            if int(s[i]) > 0:
                dp[i] = dp[i - 1]
            two_digit = int(s[i - 1: i + 1])
            if two_digit < 10 or two_digit > 26:
                continue
            dp[i] += dp[i - 2] if i > 1 else 1

        return dp[-1]