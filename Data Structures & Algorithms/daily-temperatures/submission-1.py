class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                top = st.pop()
                res[top[1]] = i - top[1]
            st.append((t, i))
        return res