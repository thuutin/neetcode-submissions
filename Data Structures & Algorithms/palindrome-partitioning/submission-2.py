class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromeIndexes = defaultdict(list)
        def check(substring):
            i = 0
            j = len(substring) - 1
            while i < j:
                if substring[i] != substring[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        for i in range(len(s)):
            for j in range(i, len(s)):
                if check(s[i:j+1]):
                    palindromeIndexes[i].append(j)  
        res = []
        def backtrack(i, substrings):
            if i >= len(s):
                res.append(substrings[:])
                return None
            for j in palindromeIndexes[i]:
                substrings.append(s[i:j + 1])
                backtrack(j + 1, substrings)
                substrings.pop()
        backtrack(0, [])
        return res