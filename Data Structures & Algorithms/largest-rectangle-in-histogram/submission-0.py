class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right = [len(heights)] * len(heights)
        left = [-1] * len(heights)
        st = []
        for i in range(len(heights) - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        st = []
        for i in range(len(heights)):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        maxArea = 0
        ##print(right)
        ##print(left)
        for i in range(len(heights)):
            width = (right[i] - 1) - (left[i] + 1) + 1
            maxArea = max(width * heights[i], maxArea)
        return maxArea