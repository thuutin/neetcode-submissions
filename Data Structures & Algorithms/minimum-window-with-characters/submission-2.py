class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        res = None
        tF = defaultdict(int)
        for c in t:
            tF[c] += 1
        windowF = defaultdict(int)
        def is_valid(windowF, tF):
            for k, v in tF.items():
                if windowF[k] < v:
                    return False
            return True
        while j < len(s):
            windowF[s[j]] += 1
            while i <= j and is_valid(windowF, tF):
                if res == None or res[1] - res[0] > j - i + 1:
                    res = i, j + 1
                windowF[s[i]] -= 1
                i += 1
            j += 1
        if res is None:
            return ""
        return s[res[0]:res[1]]
        