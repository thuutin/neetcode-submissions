class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        # dp[i] = dp[i - 1]
        # dp[i] += dp[i - 2] #if s[i - 1:i + 1] is 10 -> 26
        
        for i in range( len(s)):
            if int(s[i]) > 0:
                if i == 0:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 1]
            if i == 0:
                continue
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]