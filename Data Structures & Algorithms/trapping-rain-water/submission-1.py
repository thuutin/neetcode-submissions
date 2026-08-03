class Solution:
    def trap(self, heights: List[int]) -> int:
        maxFromRight = [-1] * len(heights)
        for i in range(len(heights) - 2, -1, -1):
            maxFromRight[i] = max(maxFromRight[i + 1], heights[i + 1])
        maxFromLeft = -1
        water = 0
        for i in range(len(heights)):
            smallWall = min(maxFromLeft, maxFromRight[i])
            water += max(0, smallWall - heights[i])
            maxFromLeft = max(maxFromLeft, heights[i])
        return water
