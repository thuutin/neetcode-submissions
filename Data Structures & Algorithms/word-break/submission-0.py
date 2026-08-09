class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        from functools import cache
        @cache
        def f(i):
            if i >= len(s):
                return True
            j = i + 1
            while j <= len(s):
                word = s[i:j]
                if word in wordDict and f(j):
                    return True
                j += 1 
            return False
        return f(0)