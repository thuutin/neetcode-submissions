class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in '[({':
                st.append(c)
            else:
                if not st:
                    return False
                cc = st.pop()
                if cc + c in ["()", "[]", "{}"]:
                    continue
                else:
                    return False
        return len(st) == 0