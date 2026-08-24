class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key = len)
        for i in range(len(strs[0])):
            p = strs[0][:i + 1]
            for s in strs:
                if s.startswith(p):
                    continue
                else:
                    return strs[0][:i]
        return strs[0]