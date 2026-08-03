class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = 0
        while i < j:
            maxArea = max(maxArea, min(heights[i], heights[j]) * (j - i))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxArea