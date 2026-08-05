class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        a = set()
        for c in range(ord('a'), ord('z') + 1):
            d = ord('A') - ord('a')
            a.add(chr(c))
            a.add(chr(c + d))
        for d in range(0, 10):
            a.add(str(d))
        def valid(c):
            return c in a

        while i < j:
            if not valid(s[i]):
                i += 1
                continue
            if not valid(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True