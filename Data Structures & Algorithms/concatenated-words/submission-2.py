class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        wordSet = set(words)
        from functools import cache
        @cache
        def exists(w, needsSplit):
            if not needsSplit and w in wordSet:
                return True
            for i in range(1, len(w)):
                left = w[:i]
                right = w[i:]
                if exists(left, False) and exists(right, False):
                    return True
            return False
        res = []
        for word in wordSet:
            if exists(word, True):
                res.append(word)
        return res
            