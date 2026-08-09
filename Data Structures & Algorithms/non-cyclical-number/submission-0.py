class Solution:
    def isHappy(self, n: int) -> bool:
        s = set([n])
        while True:
            ss = 0
            for d in str(n):
                ss += int(d) ** 2
            print(n, ss)
            n = ss
            
            if n == 1:
                return True
            if n in s:
                return False
            s.add(n)
        return None