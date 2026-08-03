class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        chars = set()
        size = 0
        while j < len(s):
            c = s[j]
            if c in chars:
                while s[i] != c:
                    chars.remove(s[i])
                    i += 1
                chars.remove(s[i])
                i += 1
            else:
                chars.add(c)
                j += 1
            size = max(size, j - i)
        return size