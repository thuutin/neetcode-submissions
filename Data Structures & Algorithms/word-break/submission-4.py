class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * len(s)
        for j in range(len(s)):
            for i in range(j, max(0, j - 20) - 1, -1):
                word = s[i:j+1]
                can_break = word in wordDict and (dp[i-1] if i >= 1 else True)
                dp[j] = can_break
                if can_break:
                    break
        return dp[-1]