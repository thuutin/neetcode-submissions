class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        sub = set()
        last_index = {}

        for i in range(len(s)):
            c = s[i]
            last_index[c] = i
        sub = set()
        i = 0
        while i < len(s):
            end = i
            j = i
            while j <= end:
                sub.add(s[j])
                end = max(end, last_index[s[j]])
                j += 1
            res.append(j - i)
            i = end + 1
        return res