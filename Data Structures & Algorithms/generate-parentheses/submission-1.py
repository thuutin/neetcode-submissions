class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = deque([("", 0)])
        res = []
        while q:
            s, left = q.popleft()
            if len(s) == n * 2:
                if left == 0:
                    res.append(s)
                continue
            q.append((s + "(", left + 1))
            if left > 0:
                q.append((s + ")", left - 1))
        return res
