class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = 0
        while i < j:
            area = min(heights[j], heights[i]) * (j - i)
            maxArea = max(area, maxArea)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return maxArea