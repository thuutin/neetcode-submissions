class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        maxSize = 0
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
                if dp[(i, j)]:
                    maxSize = max(maxSize, size)
                i += 1
        it = None
        for (i, j), v in dp.items():
            if not v:
                continue
            size = j - i + 1
            if size == maxSize:
                it = s[i:j + 1]
                break
        return it