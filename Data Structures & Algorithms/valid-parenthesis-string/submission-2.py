class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = deque()
        opened = []
        for i, c in enumerate(s):
            if c == '(':
                opened.append(i)
            elif c == ')':
                if opened:
                    opened.pop()
                elif stars:
                    stars.popleft()
                else:
                    return False
            else:
                stars.append(i)
        while opened:
            if not stars:
                return False
            if opened.pop() > stars.pop():
                return False
        return True
