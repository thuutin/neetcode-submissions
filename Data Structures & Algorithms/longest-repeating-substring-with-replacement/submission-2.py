class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j = 0
        i = 0
        size = 0
        def replacement_needed(counts):
            return sum(counts.values()) - max(counts.values())
        counts = defaultdict(int)
        while j < len(s):
            counts[s[j]] += 1
            while replacement_needed(counts) > k:
                counts[s[i]] -= 1
                i += 1
            size = max(size, j - i + 1)
            j += 1
                
        return size