class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(abbr):
            if j >= len(word):
                return False
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                num = 0 
                while i < len(abbr) and abbr[i].isdigit():
                    num = num * 10 + int(abbr[i])
                    i += 1
                j += num
            elif word[j] != abbr[i]:
                return False
            else:
                i += 1
                j += 1
        return j == len(word)