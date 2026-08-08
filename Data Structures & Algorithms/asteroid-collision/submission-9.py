class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        i = 0
        while i < len(asteroids):
            x = asteroids[i]
            if st and st[-1] > 0 and x < 0:
                if st[-1] < abs(x):
                    st.pop()
                    continue
                elif st[-1] == abs(x):
                    st.pop()
                    i += 1
                    continue
                else:
                    i += 1
                    continue
            i += 1
            st.append(x)
            
        return st