class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)
        maxLength = len(max(wordDict, key = len))

        def backtrack(i, sentence):
            if i >= len(s):
                return res.append(" ".join(sentence))
            j = i + 1
            while j <= len(s) and j - i <=  maxLength:
                word = s[i:j]
                if word in wordDict:
                    sentence.append(word)
                    backtrack(j, sentence)
                    sentence.pop()
                j += 1
        
            return None 
        backtrack(0, [])
        return res