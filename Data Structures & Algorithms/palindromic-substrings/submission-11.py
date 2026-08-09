class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(i, j):
            ss = 0
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                ss += 1
                i -= 1
                j += 1
            return ss
                
        
        sss = 0
        for i in range(len(s)):
            sss += count(i, i)
            if i + 1< len(s):
                sss += count(i, i + 1)
        return sss