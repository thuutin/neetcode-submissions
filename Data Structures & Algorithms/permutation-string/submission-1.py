class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = defaultdict(int)
        for c in s1:
            f1[c] += 1
        s = len(s1)
        f = defaultdict(int)
        for i in range(len(s2)):
            f[s2[i]] += 1
            if i - s >= 0:
                f[s2[i - s]] -= 1
                if f[s2[i - s]] == 0:
                    del f[s2[i - s]]
            
            if f1 == f:
                return True
            
        return False
            


            