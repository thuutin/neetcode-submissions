class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        for size in range(1, len(s) + 1):
            i = 0
            while i + size - 1 < len(s):
                j = i + size - 1
                if size == 1:
                    dp[(i,j)] = True
                elif size == 2:
                    dp[(i,j)] = s[i] == s[j]
                else:
                    dp[(i,j)] = s[i] == s[j] and dp[(i+1, j - 1)]
                i += 1
        #print(dp)
        it = None
        maxSize = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                size = j - i + 1
                if not dp[(i, j)]:
                    continue
                if size > maxSize:
                    maxSize = size
                    it = s[i:j + 1]
        return it