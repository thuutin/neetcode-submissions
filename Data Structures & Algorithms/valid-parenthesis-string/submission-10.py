class Solution:
    def checkValidString(self, s: str) -> bool:
        opened = 0
        flexOpen, flexClose = 0, 0
        for c in s:
            if c == '(':
                flexClose = min(opened, flexClose)
                opened += 1
            elif c == ')':
                if opened > 0:
                    opened -= 1
                elif flexOpen > 0:
                    flexClose -= 1
                    flexOpen -= 1
                else:
                    return False
            else:
                flexOpen += 1
                flexClose += 1
        return flexClose >= opened