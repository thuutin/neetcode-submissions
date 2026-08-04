class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j = 0
        i = 0
        size = 0
        counts = defaultdict(int)
        while j < len(s):
            counts[s[j]] += 1
            while sum(counts.values()) - max(counts.values()) > k:
                counts[s[i]] -= 1
                if counts[s[i]] == 0:
                    del counts[s[i]]
                i += 1
            size = max(size, j - i + 1)
            j += 1
                
        return size