class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if st and st[-1][0] == c:
                t = st.pop()[1]
                st.append((c, t + 1))
            else:
                st.append((c, 1))
            if st[-1][1] == k:
                st.pop()
        res = []
        for c, t in st:
            res.append(c * t)
        return "".join(res)