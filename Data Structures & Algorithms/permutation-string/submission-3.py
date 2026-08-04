class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = defaultdict(int)
        for c in s1:
            f1[c] += 1
        s = len(s1)
        f = defaultdict(int)
        for i in range(len(s2)):
            f[s2[i]] += 1
            if i >= s:
                c = s2[i - s]
                f[c] -= 1
                if f[c] == 0:
                    del f[c]
            if f1 == f:
                return True
        return False
            


            