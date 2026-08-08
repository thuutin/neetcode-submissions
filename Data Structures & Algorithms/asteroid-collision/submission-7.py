class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for x in asteroids:
            skip = False
            while st:
                if st[-1] * x > 0:
                    break
                if x > 0:
                    break
                if st[-1] < abs(x):
                    st.pop()
                elif st[-1] == abs(x):
                    st.pop()
                    skip = True
                    break
                else:
                    skip = True
                    break
            if not skip:
                st.append(x)
            
        return st