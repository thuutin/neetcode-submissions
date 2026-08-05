class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = defaultdict(int)
        for c in s:
            S[c] += 1
        for c in t:
            S[c] -= 1
            if S[c] == 0:
                del S[c]
        return len(S) == 0