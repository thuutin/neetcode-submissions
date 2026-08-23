class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_index = {}
        for i in range(len(s)):
            c = s[i]
            last_index[c] = i
        def find_substring_end(i):
            end = i
            j = i
            while j <= end:
                end = max(end, last_index[s[j]])
                j += 1
            return end
        i = 0
        while i < len(s):
            end = find_substring_end(i)
            res.append(end - i + 1)
            i = end + 1
        return res