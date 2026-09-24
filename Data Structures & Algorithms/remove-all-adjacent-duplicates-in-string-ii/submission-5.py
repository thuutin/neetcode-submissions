class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if st and st[-1][0] == c:
                t = st.pop()[1]
                if t == k - 1:
                    continue
                st.append((c, t + 1))
            else:
                st.append((c, 1))

        #res = []
        #for c, t in st:
        #    res.append(c * t)
        return "".join(map(lambda x: x[0] * x[1], st))