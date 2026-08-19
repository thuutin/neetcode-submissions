class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [0]
        left = [-1] * len(heights) # -1, -1, 1, ,1, 1, 4
        right = [len(heights)] * len(heights) # [1, 6, 3, 6, 6, 6]

        for i in range(1, len(heights)):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            else:
                left[i] = -1
            st.append(i)
        st = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            else:
                right[i] = len(heights)
            st.append(i)
        area = 0
        for i in range(len(heights)):
            l, r = left[i], right[i]
            a =heights[i] * (r - l - 1 )
            area = max(a, area)
        return area