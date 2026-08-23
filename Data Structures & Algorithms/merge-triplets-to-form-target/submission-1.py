class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        foundX, foundY, foundZ = False, False, False
        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            foundX = foundX or a == x
            foundY = foundY or b == y
            foundZ = foundZ or c == z
        return foundX and foundY and foundZ