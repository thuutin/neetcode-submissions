class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = 0
        while i < j:
            left = heights[i] 
            right = heights[j]
            area = min(left, right) * (j - i)
            maxArea = max(maxArea, area)
            if left < right :
                i += 1
            else:
                j -= 1
        return maxArea