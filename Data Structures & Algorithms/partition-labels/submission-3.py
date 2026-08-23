class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_index = {}
        for i in range(len(s)):
            c = s[i]
            last_index[c] = i
        def find_substring_end(i):
            j = i
            while i <= j:
                j = max(j, last_index[s[i]])
                i += 1
            return j
        i = 0
        while i < len(s):
            end = find_substring_end(i)
            res.append(end - i + 1)
            i = end + 1
        return res