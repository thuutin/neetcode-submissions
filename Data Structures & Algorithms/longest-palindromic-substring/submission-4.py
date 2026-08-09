class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        for size in range(1, len(s) + 1):
            i = 0
            while i + size - 1 < len(s):
                j = i + size - 1
                if size == 1:
                    dp[(i,j)] = True
                elif size == 2 or size == 3:
                    dp[(i,j)] = s[i] == s[j]
                else:
                    dp[(i,j)] = s[i] == s[j] and dp[(i+1, j - 1)]
                i += 1
        it = None
        maxSize = 0
        for k, v in dp.items():
            if not v:
                continue
            i, j = k
            size = j - i + 1
            if size > maxSize:
                maxSize = size
                it = s[i:j + 1]
        return it